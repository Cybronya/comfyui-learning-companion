---
name: text_to_image_upscale_lora_sampler_12
type: Text To Image
frequency: 12
level: moderate
coverage: 0.89325
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/LEO-Qwen千问文生图+一键自动角色三视图工作流_2066384439432802305.json, 图片生成/文生图/QWEN2512文生图（4步）极速_2008801134533677058.json, 图片生成/文生图/QWEN文生图（4步）极速_1995449450854277122.json, 图片生成/文生图/QWEN文生图（4步）极速_1996499117574602754.json, 图片生成/文生图/QWEN文生图（4步）极速_2075420795974807553.json, 图片生成/文生图/Qwen 2512文生图（4步）极速_1991347501961949186.json, 图片生成/文生图/Qwen+2512文生图（4步）极速_2007656420396769281.json, 图片生成/文生图/Qwen-Image-基础版_2082365287453773826.json, 图片生成/文生图/Z-image超写实文生图工作流_2099335310260916225.json, 图片生成/文生图/qwen2512渲染电商工业级海报设计_2015058586715557889.json, 图片生成/文生图/冰箱贴-文生图_1996108372120387585.json, 图片生成/文生图/文生图  QWEN2512 高清放大图_2008816043917058050.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/LEO-Qwen千问文生图+一键自动角色三视图工作流_2066384439432802305.json、图片生成/文生图/QWEN2512文生图（4步）极速_2008801134533677058.json、图片生成/文生图/QWEN文生图（4步）极速_1995449450854277122.json、图片生成/文生图/QWEN文生图（4步）极速_1996499117574602754.json、图片生成/文生图/QWEN文生图（4步）极速_2075420795974807553.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 9/12 个有
- `VAEEncodeTiled` —— 9/12 个有
- `PreviewImage` —— 8/12 个有
- `CFGNorm` —— 2/12 个有
- `FluxKontextImageScale` —— 1/12 个有
- `ImageFromBatch` —— 1/12 个有
- `Node Collector (rgthree)` —— 1/12 个有
- `SmartImageConcat` —— 1/12 个有
- `TextEncodeQwenImageEditPlus` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1080 - 1920 | 12 | 78% |
| 高度 | 1080 | 1080 - 1920 | 12 | 72% |
| 采样步数 | 6 | 4 - 10 | 12 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 83% |
| 调度器 | simple | - | 12 | 83% |
| 重绘幅度 | 1 | 0.3 - 1 | 12 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 1080 - 1920，12 个样本
- 高度 中位数 1080，观测区间 1080 - 1920，12 个样本
- 采样步数 中位数 6，观测区间 4 - 10，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 83%
- 调度器 最常用 simple，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，12 个样本
- 高发问题（24/12 个样本）：Steps较低可能导致细节不足
