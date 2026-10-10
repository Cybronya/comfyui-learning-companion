---
key: 视频生成/文生视频/AI Video Studio 专用短视频生成Seedance 2.5 工作流_2107686960369324033.json
name: AI Video Studio 专用短视频生成Seedance 2.5 工作流_2107686960369324033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI Video Studio 专用短视频生成Seedance 2.5 工作流_2107686960369324033.json
hash: 390afced8a429504
coverage: 0.857143
learned_at: 2026-10-10 22:58:30
nodes: [CR Prompt Text, TextConcatenate_UTK, TextConcatenate_UTK, easy boolean, LazySwitchKJ_UTK, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy boolean, LazySwitchKJ_UTK, RH_BytedanceSeedance25TokenMultimodalVideo, RH_Upscale, SaveVideo, LayerUtility: PurgeVRAM V2, Note, LoadAudio, LoadAudio, LoadAudio, LoadAudio, LoadAudio, CR Text, CR Prompt Text]
patterns: []
missing: [CR Text, LayerUtility: PurgeVRAM V2, easy boolean, easy boolean, CR Prompt Text, CR Prompt Text]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/AI Video Studio 专用短视频生成Seedance 2.5 工作流_2107686960369324033.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI Video Studio 专用短视频生成Seedance 2.5 工作流_2107686960369324033.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（49 个）：
- `CR Prompt Text`
- `TextConcatenate_UTK`
- `TextConcatenate_UTK`
- `easy boolean`
- `LazySwitchKJ_UTK`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy boolean`
- `LazySwitchKJ_UTK`
- `RH_BytedanceSeedance25TokenMultimodalVideo`
- `RH_Upscale`
- `SaveVideo`
- `LayerUtility: PurgeVRAM V2`
- `Note`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `CR Text`
- `CR Prompt Text`

## 知识

覆盖率 **86%**（42/49）

**有卡**：`TextConcatenate_UTK`、`LazySwitchKJ_UTK`、`LoadImage`、`RH_BytedanceSeedance25TokenMultimodalVideo`、`RH_Upscale`、`SaveVideo`、`LoadAudio`

**缺卡**（6）：`CR Text`、`LayerUtility: PurgeVRAM V2`、`easy boolean`、`easy boolean`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：LoadImage、RH_BytedanceSeedance25TokenMultimodalVideo、RH_Upscale、SaveVideo、LoadAudio、TextConcatenate_UTK、LazySwitchKJ_UTK、sd15-t2i-basic

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
