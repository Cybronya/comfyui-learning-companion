---
name: unknown_workflow_sampler_unet_vae_164
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.90875
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/千问2.1高质量快速出图_2115647178181005314.json, 图片生成/图生图/千问_2104563424893161474.json, 图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json, 图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json, 图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json, 图片生成/图生图/千问工作流_2102311506384867330.json, 图片生成/图生图/自动抠图 Qwen-image2.1_2112044955593166850.json, 数字人/数字人/千问工作流_2102229006685917186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_164

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/千问2.1高质量快速出图_2115647178181005314.json、图片生成/图生图/千问_2104563424893161474.json、图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json、图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json、图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `ResolutionSelector` —— 5/8 个有
- `EmptyImage` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `LayerUtility: TextJoin` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 35 | 8 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 8 | 100% |
| 高度 | 1024 | 1024 - 1624 | 8 | 79% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 35，8 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1624，8 个样本
