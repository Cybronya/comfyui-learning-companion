---
name: unknown_workflow_clip_unet_vae_6
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.941875
common_nodes: [CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Ai一键生成表情包_1909419548767100930.json, 图片生成/文生图/FLUX IP ADAPATER (XLABS)_1870006167324758017.json, 图片生成/文生图/FLUX 高清产品背景图生成_1921046708803796993.json, 图片生成/文生图/FLUX文生图+LoRA_1920589333093617666.json, 图片生成/文生图/FLUX文生图_1942817552894464001.json, 图片生成/文生图/FLUX文生图_1952603918469672962.json, 图片生成/文生图/FLUX超写实（文生图）_2038134888506859521.json, 图片生成/文生图/九宫格 表情包_1909435534924460034.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Ai一键生成表情包_1909419548767100930.json、图片生成/文生图/FLUX IP ADAPATER (XLABS)_1870006167324758017.json、图片生成/文生图/FLUX 高清产品背景图生成_1921046708803796993.json、图片生成/文生图/FLUX文生图+LoRA_1920589333093617666.json、图片生成/文生图/FLUX文生图_1942817552894464001.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `KSampler` —— 7/8 个有
- `PreviewImage` —— 4/8 个有
- `FluxGuidance` —— 2/8 个有
- `LoraLoader` —— 2/8 个有
- `TTP_Image_Tile_Batch` —— 2/8 个有
- `XlabsSampler` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1400 | 8 | 84% |
| 高度 | 1088 | 768 - 1600 | 8 | 77% |
| 采样步数 | 35 | 20 - 38 | 7 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 0.575 | - | 2 | 61% |
| LoRA 文本强度 | 0.9 | - | 2 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1400，8 个样本，取值集中（一致性 84%）
- 高度 中位数 1088，观测区间 768 - 1600，8 个样本
- 采样步数 中位数 35，观测区间 20 - 38，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.575，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
