---
name: unknown_workflow_video_lora_sampler_417
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.885286
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfyNumberConvert, EmptyMiniMaxH3LatentAV, ImageResizeKJv2, KSamplerSelect, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxChunkFeedForward, MiniMaxH3AddGuide, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/H3 视频修复与并排对比_2119876636576407554.json, 平台全量/MiniMax H3 老视频修复 LMS_2097647478312103938.json, 平台全量/Minimax H3-模糊视频修复_2097684309175005185.json, 平台全量/minimax_h3_lms_使用lora高清锐化视频_2110702058058895362.json, 平台全量/minimax_h3_lms_高清锐化视频修复_2099792798244499458.json, 平台全量/模糊视频修复--Minimax H3 画面重绘_2104077927523639298.json, 平台全量/视频修复-LMS_2101263013524365314.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_417

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/H3 视频修复与并排对比_2119876636576407554.json、平台全量/MiniMax H3 老视频修复 LMS_2097647478312103938.json、平台全量/Minimax H3-模糊视频修复_2097684309175005185.json、平台全量/minimax_h3_lms_使用lora高清锐化视频_2110702058058895362.json、平台全量/minimax_h3_lms_高清锐化视频修复_2099792798244499458.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `EmptyMiniMaxH3LatentAV`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3AddGuide`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 5/7 个有
- `ImageConcatMulti` —— 5/7 个有
- `ImageFromBatch` —— 5/7 个有
- `ModelPreviewOverrideKJ` —— 5/7 个有
- `VHS_LoadVideo` —— 5/7 个有
- `AddLabel` —— 3/7 个有
- `CreateVideo` —— 3/7 个有
- `ImageBatch` —— 3/7 个有
- `ImageScale` —— 3/7 个有
- `RepeatImageBatch` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `SomethingToString` —— 3/7 个有
- `StringConcatenate` —— 3/7 个有
- `Label (rgthree)` —— 2/7 个有
- `VHS_LoadVideoFFmpeg` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
