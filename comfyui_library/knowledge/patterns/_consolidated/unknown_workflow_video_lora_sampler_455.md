---
name: unknown_workflow_video_lora_sampler_455
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.59875
common_nodes: [Any Switch (rgthree), AutoCropFaces, BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, Fast Groups Bypasser (rgthree), Fast Muter (rgthree), GetImagesFromBatchIndexed, GetNode, GetVideoComponents, ImageConcatFromBatch, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/H3制作角色资产四视图角色卡1_直连修正_2102282609287065601.json, 图片生成/图生图/H3制作角色资产四视图角色卡超强一致性详拆工作流08集_2098405173931630594.json, 图片生成/图生图/Minimax H3--AI短剧人物设定多视图_2098636265678794754.json, 图片生成/图生图/Minimax h3 高一致性-人物四视图快速处理V2.0(PLUS)_2107343809830023169.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_455

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/H3制作角色资产四视图角色卡1_直连修正_2102282609287065601.json、图片生成/图生图/H3制作角色资产四视图角色卡超强一致性详拆工作流08集_2098405173931630594.json、图片生成/图生图/Minimax H3--AI短剧人物设定多视图_2098636265678794754.json、图片生成/图生图/Minimax h3 高一致性-人物四视图快速处理V2.0(PLUS)_2107343809830023169.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `AutoCropFaces`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `Fast Muter (rgthree)`
- `GetImagesFromBatchIndexed`
- `GetNode`
- `GetVideoComponents`
- `ImageConcatFromBatch`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有
- `SeedVR2LoadDiTModel` —— 2/4 个有
- `SeedVR2LoadVAEModel` —— 2/4 个有
- `SeedVR2VideoUpscaler` —— 2/4 个有
- `workflow>SeedVR放大节点` —— 2/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `LayerUtility: SaveImagePlus` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有
- `VOSR2ModelLoader` —— 1/4 个有
- `VOSR2Upscale` —— 1/4 个有
- `easy float` —— 1/4 个有
- `easy int` —— 1/4 个有
- `孤海注释` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
