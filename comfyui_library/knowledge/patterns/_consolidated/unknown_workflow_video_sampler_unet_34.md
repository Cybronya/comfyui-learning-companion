---
name: unknown_workflow_video_sampler_unet_34
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.885875
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MinimaxH3-10EROS三宫格分镜美学强化_2086655149459726337.json, 视频生成/图生视频/MinimaxH3-10EROS美学强化视频_2086457099797753858.json, 视频生成/图生视频/MinimaxH3清凉一夏_2087214218717261826.json, 视频生成/图生视频/MinimaxH3漫剧场景T2_2084831798504288258.json, 视频生成/图生视频/MinimaxH3电影感视频生成T1_2085396097698193409.json, 视频生成/图生视频/minimaxH3人物运镜_2087416252800262146.json, 视频生成/图生视频/minimaxH3多参提示词优化_2085352355951894530.json, 视频生成/图生视频/minimaxh3全参连续帧提示词自动优化_2085978725648261121.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_34

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3-10EROS三宫格分镜美学强化_2086655149459726337.json、视频生成/图生视频/MinimaxH3-10EROS美学强化视频_2086457099797753858.json、视频生成/图生视频/MinimaxH3清凉一夏_2087214218717261826.json、视频生成/图生视频/MinimaxH3漫剧场景T2_2084831798504288258.json、视频生成/图生视频/MinimaxH3电影感视频生成T1_2085396097698193409.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/8 个有
- `ResolutionSelector` —— 6/8 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 6/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/8 个有
- `ImageConcatenateMulti_UTK` —— 3/8 个有
- `easy imageSplitGrid` —— 3/8 个有
- `easy indexAnything` —— 3/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `LoadAudio` —— 2/8 个有
- `MiniMaxH3ImageToVideo` —— 2/8 个有
- `easy showAnything` —— 2/8 个有
- `1hew_AudioDuration` —— 1/8 个有
- `Bjornulf_ShowFloat` —— 1/8 个有
- `LoadVideoUI` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
