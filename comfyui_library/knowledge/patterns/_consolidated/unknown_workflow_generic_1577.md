---
name: unknown_workflow_generic_1577
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8595
common_nodes: [1hew_SaveTxt, BreakGrid, CR Prompt Text, Fast Groups Bypasser (rgthree), JWStringConcat, LoadImage, Qwen3_VQA, RH_LLMAPI_Pro_Node, SaveImage, StringConcat|Mie, StringConstant, Text List Concatenate, Text Multiline, easy indexAnything, easy promptList, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/连环画提取转绘及视频提示词Gemini3Pro_2051896794396803073.json, 图片生成/图生图/连环画提取转绘及视频提示词Gemma4+全能图片G2Image_2072736727537639425.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1577

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/连环画提取转绘及视频提示词Gemini3Pro_2051896794396803073.json、图片生成/图生图/连环画提取转绘及视频提示词Gemma4+全能图片G2Image_2072736727537639425.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `1hew_SaveTxt`
- `BreakGrid`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `JWStringConcat`
- `LoadImage`
- `Qwen3_VQA`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `StringConcat|Mie`
- `StringConstant`
- `Text List Concatenate`
- `Text Multiline`
- `easy indexAnything`
- `easy promptList`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `GetImagesFromBatchIndexed` —— 1/2 个有
- `Image Padding` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `SaveImageAdvanced` —— 1/2 个有
- `SaveText` —— 1/2 个有
- `YM_GPT_image2_0` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
