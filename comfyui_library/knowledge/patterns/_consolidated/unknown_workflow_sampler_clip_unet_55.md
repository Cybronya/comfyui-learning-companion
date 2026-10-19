---
name: unknown_workflow_sampler_clip_unet_55
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.943
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [MathExpression|pysssss, easy cleanGpuUsed]
members: [图片生成/文生图/1950957566572568577.json, 图片生成/文生图/1957777125837303810.json, 视频生成/图生视频/1950898146819899393.json, 视频生成/图生视频/1956152665396969474.json, 视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_55

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/1950957566572568577.json、图片生成/文生图/1957777125837303810.json、视频生成/图生视频/1950898146819899393.json、视频生成/图生视频/1956152665396969474.json、视频生成/文生视频/Wan2.2文生视频_2020007175808094210.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `EmptyHunyuanLatentVideo` —— 4/5 个有
- `SaveVideo` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `PathchSageAttentionKJ` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `Int` —— 2/5 个有
- `ModelPatchTorchSettings` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有
- `VHS_VideoCombine` —— 1/5 个有
- `WanFunInpaintToVideo` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 20 | 6 - 20 | 5 | 60% |
| 采样算法 | 3.5 | 1 - 3.5 | 5 | 51% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 20，观测区间 6 - 20，5 个样本
- 采样算法 中位数 3.5，观测区间 1 - 3.5，5 个样本
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 80%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、easy cleanGpuUsed
