---
name: unknown_workflow_video_sampler_unet_31
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.548818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json, 图片生成/图生图/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2099794040656060418.json, 图片生成/文生图/MiniMax H3 Ref2VA｜6图多参考·角色一致性·Sage加速_2087595496494948354.json, 图片生成/文生图/MiniMax H3 短剧生成 _ 9图3音色参考 _ 省算力高动态加速版_2091615916835557378.json, 数字人/数字人/优化版本新版口播_2108152027493785602.json, 数字人/数字人/新版本口播_2107771154403520513.json, 视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json, 视频生成/图生视频/AITUDOU-MiniMax H3 打斗-单采_2095430334602113026.json, 视频生成/图生视频/MiniMax H3-单采_2102816230406189058.json, 视频生成/图生视频/MiniMax_H3-单采_2106176867115036673.json, 视频生成/文生视频/官方 全能参考版单采_2104530172652380161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_31

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json、图片生成/图生图/人像VLOG丨MiniMax-H3丨三图参考·音画生成_2099794040656060418.json、图片生成/文生图/MiniMax H3 Ref2VA｜6图多参考·角色一致性·Sage加速_2087595496494948354.json、图片生成/文生图/MiniMax H3 短剧生成 _ 9图3音色参考 _ 省算力高动态加速版_2091615916835557378.json、数字人/数字人/优化版本新版口播_2108152027493785602.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `Text` —— 10/11 个有
- `VAEDecode` —— 10/11 个有
- `VAEDecodeAudio` —— 10/11 个有
- `GetNode` —— 9/11 个有
- `SetNode` —— 9/11 个有
- `Float` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 5/11 个有
- `LoadAudio` —— 5/11 个有
- `ModelAttentionBackend` —— 5/11 个有
- `PrimitiveFloat` —— 4/11 个有
- `ExtendIntermediateSigmas` —— 3/11 个有
- `H3SigmaRefiner` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/11 个有
- `AudioSeparation` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `MiniMaxH3AddGuide` —— 2/11 个有
- `SplitSigmas` —— 2/11 个有
- `VHS_LoadVideo` —— 2/11 个有
- `EmptyImage` —— 1/11 个有
- `ImageResizeKJv2` —— 1/11 个有
- `ImageScaleToTotalPixels` —— 1/11 个有
- `MiniMaxH3AVDecodeT8` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `SigmasGraph` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
