import{Box,Heading,VStack,Input,Img,Link,Button,Flex,Text}from'@chakra-ui/react';
import Register from './Register';

export default function Login(){
    return(
        
<Box
position= 'absolute'
width= '720px'
height= '900px'
left= '-1px'
top='0px'
background= '#FFFFFF'
>
<VStack >
   <Box
    position= 'absolute'
    width='533px'
    height='77px'
    left='102px'
    top= '210px'
    fontFamily= 'Cinzel'
    fontStyle= 'normal'
    fontWeight= '500'
    fontSize= '64px'
    textAlign= 'center'
    letterSpacing= '-0.02em'
    lineHeight= '86px'
    alignSelf='center'
    alignItems= 'center'
    color= '#000000'>LOGIN </Box>

<Input 
fontFamily= 'EB Garamond'
fontSize= '24px'
fontWeight= '400'
lineHeight= '31px'
letterSpacing= '-0.02em'
textAlign= 'left'
color='#1E1E1E'
position= 'absolute'
width= '588.77px'
height= '44.21px'
left= '65px'
top= '333.79px'
background= '#D9D9D9'
borderRadius='5px'
 rounded='1' variant='filled' type='text' placeholder='Username'/>

<Input 
fontFamily= 'EB Garamond'
fontSize= '24px'
fontWeight= '400'
lineHeight= '31px'
letterSpacing= '-0.02em'
textAlign= 'left'
color='#1E1E1E'
position= 'absolute'
width= '588.77px'
height= '44.21px'
left= '65px'
top= '414.63px'
background= '#D9D9D9'
borderRadius= '5px'
rounded='1' variant='filled' type='password' placeholder='Password'/>

<Link 
position= 'absolute'
width= '140px'
height= '26px'
left= '558px'
top= '469px'
fontFamily= 'EB Garamond'
fontSize= '16px'
fontWeight= '400'
lineHeight= '21px'
letterSpacing= '-0.02em'
textAlign= 'left'
color= '#000000'
>Forgot Password
</Link>

<Button 
background= '#61876E'
borderRadius= '7.5px'
flex='none'
order= '0'
height=' 63px'
width= '588px'
left='65px'
top= '538.42px'
position= 'absolute'
fontFamily= 'EB Garamond'
fontStyle='normal'
fontWeight= '500'
fontSize='32px'
lineHeight= '42px'
display= 'flex'
alignItems= 'center'
letterSpacing= '-2%'
color= '#FFFFFF'>Sign in
</Button>

<Button background= '#D9D9D9'
borderRadius= '7.5px'
flex='none'
order= '0'
height=' 63px'
width= '588px'
left='65px'
top= '625px'
position= 'absolute'
fontFamily= 'EB Garamond'
fontStyle='normal'
fontWeight= '500'
fontSize='32px'
lineHeight= '41.76px'
display= 'flex'
alignItems= 'center'
letterSpacing= '-2%'
color= '#000000'>Register
</Button>

</VStack>





<Box
position= 'absolute'
width= '720px'
height= '900px'
left= '720px'
top='0px'
background= '#CEEDC7'
><Img  src="./images/img1.jpeg" alt='' position='absolute'
width= '450px'
height= '342px'
left= '135px'
top= '279px'
borderRadius='7.5px'
opacity='65%'/>
</Box>
</Box>


    )
    }
    
