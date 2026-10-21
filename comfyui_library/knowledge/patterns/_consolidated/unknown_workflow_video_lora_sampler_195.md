---
name: unknown_workflow_video_lora_sampler_195
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.6288
common_nodes: [BasicGuider, BasicScheduler, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3Easy, MiniMaxH3EasyLoader, MiniMaxH3EasyOutput, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEEncode, VAEEncodeAudio, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/water-MiniMax H3 15S视频工作流_2094329733709385729.json, 视频生成/文生视频/MINImax h3_2091119331596922882.json, 视频生成/文生视频/MiniMax H3 Easy 极简工作台（多参）_2091444651705331713.json, 视频生成/文生视频/MinimaxH3 奇妙地图旅游 RH版本_2088645501947301889.json, 视频生成/文生视频/MinimaxH3 奇妙地图旅游_双人版 RH版本_2090144918969864194.json, 视频生成/文生视频/MinimaxH3 最优二采多合一工作流  林耀_2091937209892036609.json, 视频生成/文生视频/MinimaxH3 极简版风格_优化版_多合一工作流_2088650571120209921.json, 视频生成/文生视频/MinimaxH3 极简版风格_优化版_多合一工作流_2089082465007783937.json, 视频生成/文生视频/MinimaxH3全能参考V3极简版（人脸增强8步二次采样1080p）_2087773102355869698.json, 视频生成/文生视频/MinimaxH3全能参考V5电影画质去油版1_2089032793069277185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_195

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/water-MiniMax H3 15S视频工作流_2094329733709385729.json、视频生成/文生视频/MINImax h3_2091119331596922882.json、视频生成/文生视频/MiniMax H3 Easy 极简工作台（多参）_2091444651705331713.json、视频生成/文生视频/MinimaxH3 奇妙地图旅游 RH版本_2088645501947301889.json、视频生成/文生视频/MinimaxH3 奇妙地图旅游_双人版 RH版本_2090144918969864194.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3Easy`
- `MiniMaxH3EasyLoader`
- `MiniMaxH3EasyOutput`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VAEEncode`
- `VAEEncodeAudio`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `LoadVideo` —— 8/10 个有
- `VAEDecodeAudio` —— 8/10 个有
- `easy cleanGpuUsed` —— 8/10 个有
- `Text` —— 5/10 个有
- `LoadVideoNode` —— 4/10 个有
- `HAIGC_VideoLoader` —— 2/10 个有
- `MiniMaxH3AVDecodeT8` —— 2/10 个有
- `easy clearCacheAll` —— 2/10 个有
- `忽略多组孤海` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有
- `TTResolutionSelector` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
