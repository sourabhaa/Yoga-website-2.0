import{Box,Heading,VStack,Input,Img,Link,Button,Flex,Text}from'@chakra-ui/react';

export default function Register(){

    return(
<Box
position= 'absolute'
width= '720px'
height= '900px'
left= '0px'
top='0px'
background= '#CEEDC7'
><VStack spacing='30.63px' >
   <Box
    position= 'absolute'
    width='282px'
    height='86px'
    left='219px'
    top= '195px'
    fontFamily= 'Cinzel'
    fontStyle= 'normal'
    fontWeight= '500'
    fontSize= '64px'
    textAlign= 'center'
    letterSpacing= '-0.02em'
    lineHeight= '86px'
    alignSelf='center'
    alignItems= 'center'
    color= '#000000'>REGISTER </Box>
   

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
height= '55.77px'
left= '66px'
top= '281.79px'
background= '#D9D9D9'
borderRadius='5px'
 rounded='1' variant='filled' type='email' placeholder='Email'/>

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
height= '55.77px'
left= '66px'
top= '368.16px'
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
height= '55.77px'
left= '66px'
top= '449.32px'
background= '#D9D9D9'
borderRadius='5px'
 rounded='1' variant='filled' placeholder='DOB' type='calendar'></Input>


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
height= '55.77px'
left= '66px'
top= '530.32px'
background= '#D9D9D9'
borderRadius='5px'
 rounded='1' variant='filled' type='password' placeholder='Password'/>

<Button 
background= '#61876E'
borderRadius= '7.5px'
flex='none'
flexGrow='0'
order= '0'
height=' 63.16px'
width= '588.77px'
left='66px'
top= '631px'
position= 'absolute'
fontFamily= 'EB Garamond'
fontStyle='normal'
fontWeight= '500'
fontSize='32px'
lineHeight= '42px'
display= 'flex'
alignItems= 'center'
letterSpacing= '-2%'
color= '#FFFFFF'>Sign up
</Button>



</VStack>
<Box
position= 'absolute'
width= '720px'
height= '900px'
left= '720px'
top='0px'
background= '#FFFFFF'
><Img  src="./images/img2.jpeg" alt='' position='absolute'
width= '456px'
height= '349px'
left= '147px'
top= '275px'
borderRadius='7.5px'
opacity='65%'/>
    </Box>
</Box>
    )
}