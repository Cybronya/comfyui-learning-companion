---
name: unknown_workflow_sampler_unet_vae_44
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.779
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: [CR Text, 孤海图像缩放按像素, 忽略多组孤海]
members: [视频生成/图生视频/1934647540794990594.json, 视频生成/图生视频/GF02-MiniMax H3图生视频_2084710216851087361.json, 视频生成/图生视频/MINIMAX-H3-图生视频_2084159275156467714.json, 视频生成/图生视频/MINIMAX-H3-图生视频_2084308814681169921.json, 视频生成/图生视频/MiniMax H3 Start-and-End Frame Video Workflow_2090702379476930562.json, 视频生成/图生视频/MiniMax H3 全能参考｜图生视频工作流（优化版）_2090248587761512450.json, 视频生成/图生视频/MiniMax H3图生视频工作流低显存加速版 开源 FL2VA_2084432209041252353.json, 视频生成/图生视频/MiniMax H3首尾帧视频工作流低显存加速版 开源 FL2VA_2084428374197497858.json, 视频生成/图生视频/海螺H3-全自动图生视频-自动撰写提示词_2086431051328614402.json, 视频生成/文生视频/1934647540794990594.json, 视频生成/文生视频/260818001.MiniMax-H3 文生丨首尾帧生视频_2089370217431523330.json, 视频生成/文生视频/文生视频_图生视频MiniMax+H3_2084798105811251201.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_44

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1934647540794990594.json、视频生成/图生视频/GF02-MiniMax H3图生视频_2084710216851087361.json、视频生成/图生视频/MINIMAX-H3-图生视频_2084159275156467714.json、视频生成/图生视频/MINIMAX-H3-图生视频_2084308814681169921.json、视频生成/图生视频/MiniMax H3 Start-and-End Frame Video Workflow_2090702379476930562.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 9/12 个有
- `ResolutionSelector` —— 9/12 个有
- `PathchSageAttentionKJ` —— 7/12 个有
- `easy showAnything` —— 6/12 个有
- `PreviewImage` —— 5/12 个有
- `孤海注释` —— 5/12 个有
- `CR Text` —— 4/12 个有
- `Label (rgthree)` —— 4/12 个有
- `LoraLoaderModelOnly` —— 4/12 个有
- `CR Prompt Text` —— 3/12 个有
- `GoohaiUniversalSlider` —— 3/12 个有
- `MiniMaxH3BlockCacheT8` —— 3/12 个有
- `孤海图像缩放按像素` —— 3/12 个有
- `忽略多组孤海` —— 3/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、孤海图像缩放按像素、忽略多组孤海
