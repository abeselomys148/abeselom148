import Todo from "../Models/todo.models.js"
import mongoose from "mongoose"

export const getAllTodos = async(req,res,next) => {
    try {
        const todos = await Todo.find(); 

        res.status(200).json({
            success : true,
            data: todos,
        });
    } catch (error) {
        next(error) 
    } 
}

export const createTodo = async(req,res,next) => {
    const session = await mongoose.startSession();
    session.startTransaction()

    try {
        const { name,forWhen,priority } = req.body;

        const newTodo = await Todo.create([ { name,priority,forWhen }, { session } ])

        await session.commitTransaction();
        session.endSession();

        res.status(201).json({
            success: true,
            message: "Todo created succesfully",
            data: newTodo[0],

        })
    } catch (error) {
        await session.abortTransaction(); 
        session.endSession()
        next(error);
    }
}

export const updateOne = async(req,res,next) => {
    const session = await mongoose.startSession();
    session.startTransaction();

    try {
         const { id,wtBe, toBe} = req.body;   

        if (wtBe != 'name' && wtBe != "forWhen" && wtBe != "priority" ) {
            const error = new Error("unknown property");   
            error.statusCode = 404;
            throw error;
        }

        const updateTodo = await Todo.findByIdAndUpdate(
            id,
            { wtBe : toBe  },
            { new: true, runValidators: true }
        );


        if (!updateTodo) {
            const error = new Error("something went wrong");
            error.statusCode = 500;
            throw error;
        }

        await session.commitTransaction();
        session.endSession();
    } catch (error) {
        await session.abortTransaction() 
        session.endSession()
        next(error);
    }
}

export const deleteOne = async(req,res,next) => {

    try {
        const { id } = req.body;
        const result = await Todo.deletOne({ _id: id });

        if (result.deletCount === 1) {
            res.status(200).json({
                success: true
            }) 
        }
        else{
            let error = new Error("deleting was not succesful")   
            error.statusCode = 500;
            throw error;
        }
    } catch (error) {
        next(error); 
    }
}
