import { response_200, response_500 } from '../utils/responseCodes.js';
// import prisma from '../config/db.config.js';

async function outgoingScan(req, res) {
    try {
        const code = req.body.code;

        // await prisma.quiz.update({
        //     where: {
        //         quizId: quizId
        //     },
        //     data: {
        //         questions: {
        //             connect: {
        //                 questionId: newQuestion.questionId
        //             }
        //         }
        //     }
        // });

        response_200(res, 'Item decreased successfully', null);
    } catch (error) {
        console.error(`Error updating: ${error}`);
        response_500(res, 'Error updating', error);
    }
}

async function incomingScan(req, res) {
    try {
        const code = req.body.code;

        // await prisma.quiz.update({
        //     where: {
        //         quizId: quizId
        //     },
        //     data: {
        //         questions: {
        //             connect: {
        //                 questionId: newQuestion.questionId
        //             }
        //         }
        //     }
        // });

        response_200(res, 'Item increased successfully', null);
    } catch (error) {
        console.error(`Error updating: ${error}`);
        response_500(res, 'Error updating', error);
    }
}

async function getDetails(req, res) {
    try {
        const code = req.body.code;

        // await prisma.quiz.update({
        //     where: {
        //         quizId: quizId
        //     },
        //     data: {
        //         questions: {
        //             connect: {
        //                 questionId: newQuestion.questionId
        //             }
        //         }
        //     }
        // });

        response_200(res, 'Item increased successfully', null);
    } catch (error) {
        console.error(`Error updating: ${error}`);
        response_500(res, 'Error updating', error);
    }
}

export { outgoingScan, incomingScan, getDetails };

