---
name: unknown_workflow_sampler_unet_vae_67
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.843615
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3 首尾帧参考生视频8步LoRa+Sage双重加速版_2089609194008829953.json, 视频生成/图生视频/MiniMax H3 首尾帧参考生视频_2084190798547079170.json, 视频生成/图生视频/MiniMax H3 首帧参考生视频（可本地运行）_2084287439908204546.json, 视频生成/图生视频/MiniMax H3 首帧参考生视频（图生视频）8步LoRa+Sage双重加速版_2089329038178476033.json, 视频生成/图生视频/MiniMax H3 首帧参考生视频（图生视频）8步加速版_2084173473068445697.json, 视频生成/图生视频/MiniMax H3 首帧参考生视频（图生视频）_2092513283923337217.json, 视频生成/图生视频/MiniMax H3 首帧参考生视频（图生视频）工作流_2084842142773628930.json, 视频生成/图生视频/MiniMax H3+lightx2v 4步加速全能参考工作流2图_2086437276707545089.json, 视频生成/图生视频/MiniMax H3参考生视频_2088969520458321922.json, 视频生成/图生视频/MiniMax H3图片参考生成带货视频加速版_2084302463045300225.json, 视频生成/图生视频/h3  4步多图自用_2088590941430046722.json, 视频生成/图生视频/minimaxh3首尾帧视频_2109562727692849153.json, 视频生成/文生视频/MiniMax H3+lightx2v 4步加速全能参考工作流_2086324132442107906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_67

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 首尾帧参考生视频8步LoRa+Sage双重加速版_2089609194008829953.json、视频生成/图生视频/MiniMax H3 首尾帧参考生视频_2084190798547079170.json、视频生成/图生视频/MiniMax H3 首帧参考生视频（可本地运行）_2084287439908204546.json、视频生成/图生视频/MiniMax H3 首帧参考生视频（图生视频）8步LoRa+Sage双重加速版_2089329038178476033.json、视频生成/图生视频/MiniMax H3 首帧参考生视频（图生视频）8步加速版_2084173473068445697.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 10/13 个有
- `MiniMaxH3ImageToVideo` —— 8/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/13 个有
- `LoraLoaderModelOnly` —— 7/13 个有
- `ResolutionSelector` —— 7/13 个有
- `easy showAnything` —— 7/13 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/13 个有
- `MiniMaxH3ReferenceToVideo` —— 5/13 个有
- `PathchSageAttentionKJ` —— 5/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `VHS_VideoCombine` —— 4/13 个有
- `LoadAudio` —— 3/13 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 3/13 个有
- `SpectrumSDXL` —— 3/13 个有
- `easy int` —— 3/13 个有
- `ImageResize+` —— 1/13 个有
- `ImageScale` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `TESpeedMiniMaxH3` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
