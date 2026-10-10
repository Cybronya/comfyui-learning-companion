---
key: 视频生成/文生视频/Wan2.2文生视频，图生视频，首尾帧，多图参考大集合_1971602288718573570.json
name: Wan2.2文生视频，图生视频，首尾帧，多图参考大集合_1971602288718573570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频，图生视频，首尾帧，多图参考大集合_1971602288718573570.json
hash: 3ac29f39e96c5e76
coverage: 0.617647
learned_at: 2026-10-10 23:08:05
nodes: [WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoTextEncode, GetImageSizeAndCount, WanVideoSampler, WanVideoSampler, WanVideoDecode, WanVideoSetBlockSwap, VHS_VideoCombine, CreateCFGScheduleFloatList, INTConstant, INTConstant, GetNode, WanVideoEmptyEmbeds, GetNode, WanVideoTextEncode, WanVideoImageToVideoEncode, WanVideoBlockSwap, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoSetBlockSwap, WanVideoSetLoRAs, GetNode, ImageResizeKJv2, GetNode, GetNode, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoSetLoRAs, GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoContextOptions, WanVideoSampler, WanVideoDecode, WanVideoSampler, GetImageSizeAndCount, VHS_VideoCombine, GetNode, WanVideoSetBlockSwap, SimpleMath+, GetNode, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoModelLoader, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoClipVisionEncode, GetImageSizeAndCount, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, WanVideoTextEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, easy cleanGpuUsed, ImageResizeKJv2, ImageResizeKJv2, SimpleMath+, GetNode, GetNode, GetNode, GetNode, GetNode, CR Text, ImpactInt, ImpactInt, SetNode, SetNode, Note, SetNode, Note, WanVideoVRAMManagement, WanVideoDecode, ImageConcatMulti, ImagePadKJ, ImagePadKJ, WanVideoEncode, WanVideoEncode, WanVideoSampler, Note, WanVideoTeaCache, ImageResizeKJ, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, GetNode, GetNode, VHS_VideoCombine, Note, SetNode, GetNode, GetNode, ImageResizeKJ, WanVideoPhantomEmbeds, Note, Note, WanVideoTextEncode, SetNode, GetNode, SimpleMath+, GetNode, SimpleMath+, PreviewImage, WanVideoVAELoader, QwenLoader, WanVideoPromptExtender, ShowText|pysssss, INTConstant, WanVideoSampler, CreateCFGScheduleFloatList, INTConstant, WanVideoSampler, GetNode, LoadImage, Note, SetNode, LoadImage, Note, ImpactInt, SetNode, Note, Text, Note, SetNode, ImpactInt, LoadImage, Note, LoadImage, Note, Text, Note, SetNode, Note, Text, Text, SetNode, SetNode, SetNode, GetNode, SetNode, Note, Note, Fast Groups Muter (rgthree), Note, VHS_VideoCombine, CLIPVisionLoader, LoadImage]
patterns: []
missing: [CR Text, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2文生视频，图生视频，首尾帧，多图参考大集合_1971602288718573570.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2文生视频，图生视频，首尾帧，多图参考大集合_1971602288718573570.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（170 个）：
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoSetBlockSwap`
- `SimpleMath+`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoClipVisionEncode`
- `GetImageSizeAndCount`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Text`
- `ImpactInt`
- `ImpactInt`
- `SetNode`
- `SetNode`
- `Note`
- `SetNode`
- `Note`
- `WanVideoVRAMManagement`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImagePadKJ`
- `WanVideoEncode`
- `WanVideoEncode`
- `WanVideoSampler` ★核心
- `Note`
- `WanVideoTeaCache`
- `ImageResizeKJ`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJ`
- `WanVideoPhantomEmbeds`
- `Note`
- `Note`
- `WanVideoTextEncode`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `SimpleMath+`
- `PreviewImage`
- `WanVideoVAELoader`
- `QwenLoader`
- `WanVideoPromptExtender`
- `ShowText|pysssss`
- `INTConstant`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoSampler` ★核心
- `GetNode`
- `LoadImage`
- `Note`
- `SetNode`
- `LoadImage`
- `Note`
- `ImpactInt`
- `SetNode`
- `Note`
- `Text`
- `Note`
- `SetNode`
- `ImpactInt`
- `LoadImage`
- `Note`
- `LoadImage`
- `Note`
- `Text`
- `Note`
- `SetNode`
- `Note`
- `Text`
- `Text`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Note`
- `Note`
- `Fast Groups Muter (rgthree)`
- `Note`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `LoadImage`

## 知识

覆盖率 **62%**（105/170）

**有卡**：`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoEmptyEmbeds`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoLoraSelect`、`WanVideoClipVisionEncode`、`ImpactInt`、`WanVideoVRAMManagement`、`ImageConcatMulti`、`ImagePadKJ`、`WanVideoEncode`、`WanVideoTeaCache`、`ImageResizeKJ`、`WanVideoPhantomEmbeds`、`QwenLoader`、`WanVideoPromptExtender`、`LoadImage`、`Text`、`CLIPVisionLoader`

**缺卡**（11）：`CR Text`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`SimpleMath+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
