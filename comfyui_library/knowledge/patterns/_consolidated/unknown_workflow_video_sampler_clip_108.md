---
name: unknown_workflow_video_sampler_clip_108
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9038
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, ImageResize+, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1985359491870900226.json, 视频生成/图生视频/1986821092411174914.json, 视频生成/图生视频/2073253543934517249.json, 视频生成/图生视频/2073252663759818754.json, 视频生成/图生视频/2073301344374575105.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_108

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1985359491870900226.json、视频生成/图生视频/1986821092411174914.json、视频生成/图生视频/2073253543934517249.json、视频生成/图生视频/2073252663759818754.json、视频生成/图生视频/2073301344374575105.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ImageResize+`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `ColorMatch` —— 3/5 个有
- `WanFirstMiddleLastFrameToVideo` —— 3/5 个有
- `WanFirstLastFrameToVideo` —— 2/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有
- `easy batchAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
