---
name: unknown_workflow_video_clip_unet_9
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.871889
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ModelSamplingSD3, PrimitiveInt, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1980507194548469761.json, 视频生成/图生视频/1980673656160436226.json, 视频生成/图生视频/2049663225859457025.json, 视频生成/图生视频/2050777904669306881.json, 视频生成/图生视频/1983902184238710786.json, 视频生成/图生视频/1979742422047559681.json, 视频生成/图生视频/1989285733921902593.json, 视频生成/图生视频/1979871682087260162.json, 视频生成/图生视频/1993950908476309506.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1980507194548469761.json、视频生成/图生视频/1980673656160436226.json、视频生成/图生视频/2049663225859457025.json、视频生成/图生视频/2050777904669306881.json、视频生成/图生视频/1983902184238710786.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `CLIPVisionEncode` —— 7/9 个有
- `CLIPVisionLoader` —— 7/9 个有
- `KSamplerAdvanced` —— 7/9 个有
- `SimpleMath+` —— 7/9 个有
- `WanFirstLastFrameToVideo` —— 5/9 个有
- `ApplySageAttention` —— 2/9 个有
- `LoraLoaderModelOnly` —— 2/9 个有
- `PainterI2V` —— 2/9 个有
- `WanImageToVideo` —— 2/9 个有
- `WanMoeKSampler` —— 2/9 个有
- `CR SDXL Aspect Ratio` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `ImageFromBatch+` —— 1/9 个有
- `KSampler` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 56% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 9 | 100% |
| 采样算法 | 1 | 1 - 1.5 | 9 | 81% |
| 调度器 | uni_pc | - | 9 | 67% |
| 重绘幅度 | simple | - | 9 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 56%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.5，9 个样本，取值集中（一致性 81%）
- 调度器 最常用 uni_pc，9 个样本，一致性 67%
- 重绘幅度 最常用 simple，9 个样本，一致性 78%
