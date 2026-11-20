---
name: unknown_workflow_sampler_clip_checkpoint_14
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.490429
common_nodes: [CLIPTextEncodeSDXL, CheckpointLoaderSimple, DF_Integer, DF_Text_Box, EmptyLatentImage, KSamplerAdvanced, PreviewImage, VAEDecode]
problems: []
missing: []
members: [平台全量/夏日露营计划_1808789071580868610.json, 平台全量/深夜面馆_1807665555765153794.json, 平台全量/皮克斯卡通动物_1804060341881004034.json, 平台全量/粉萌版十二生肖_1804053295659999233.json, 平台全量/花幕下的猫_1808837394425688066.json, 平台全量/蘑菇蘑菇屋_1804067786657357825.json, 平台全量/跳芭蕾舞的女孩_1804048588921102338.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/夏日露营计划_1808789071580868610.json、平台全量/深夜面馆_1807665555765153794.json、平台全量/皮克斯卡通动物_1804060341881004034.json、平台全量/粉萌版十二生肖_1804053295659999233.json、平台全量/花幕下的猫_1808837394425688066.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncodeSDXL`
- `CheckpointLoaderSimple`
- `DF_Integer`
- `DF_Text_Box`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `PreviewImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 6/7 个有
- `CLIPTextEncodeSDXLRefiner` —— 5/7 个有
- `ImageUpscaleWithModel` —— 5/7 个有
- `KSampler` —— 5/7 个有
- `UpscaleModelLoader` —— 5/7 个有
- `Image Overlay` —— 2/7 个有
- `LoadImage` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 7 | 100% |
| 高度 | 512 | 512 - 512 | 7 | 100% |
| 采样步数 | randomize | - | 7 | 86% |
| Prompt 约束强度(CFG) | 45 | 6 - 45 | 7 | 65% |
| 采样算法 | 6.5 | 6.5 - 6.5 | 6 | 100% |
| 调度器 | dpmpp_3m_sde_gpu | - | 7 | 86% |
| 重绘幅度 | karras | - | 7 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 45，观测区间 6 - 45，7 个样本
- 采样算法 中位数 6.5，观测区间 6.5 - 6.5，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_3m_sde_gpu，7 个样本，一致性 86%
- 重绘幅度 最常用 karras，7 个样本，一致性 86%
- 风险：Prompt 约束强度(CFG) 观测到 45，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
