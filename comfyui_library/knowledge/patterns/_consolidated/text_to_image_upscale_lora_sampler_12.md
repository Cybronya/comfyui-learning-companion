---
name: text_to_image_upscale_lora_sampler_12
type: Text To Image
frequency: 14
level: moderate
coverage: 0.894214
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/qwen 2512  自动_手动输入提示词 图像编辑 满血版 Qwen+2512文生图（4步）极速_2006980155113218050.json, 图片生成/文生图/QWEN2512文生图（4步）极速_2008801134533677058.json, 图片生成/文生图/QWEN文生图（4步）极速_1995449450854277122.json, 图片生成/文生图/QWEN文生图（4步）极速_1996499117574602754.json, 图片生成/文生图/QWEN文生图（4步）极速_2075420795974807553.json, 图片生成/文生图/Qwen 2512文生图（4步）极速_1991347501961949186.json, 图片生成/文生图/Qwen+2512文生图（4步）极速_2007656420396769281.json, 图片生成/文生图/Seedance2.5全参工作流_2115583117993005058.json, 图片生成/文生图/Z-image超写实文生图工作流_2099335310260916225.json, 图片生成/文生图/qwen2512渲染电商工业级海报设计_2015058586715557889.json, 图片生成/文生图/z-image文生图工作流（不油腻超写实）_2099020153999675394.json, 图片生成/文生图/z-image文生图工作流（不油腻超写实）_2099402532144635906.json, 图片生成/文生图/冰箱贴-文生图_1996108372120387585.json, 图片生成/文生图/文生图  QWEN2512 高清放大图_2008816043917058050.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_12

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/反推提示词/qwen 2512  自动_手动输入提示词 图像编辑 满血版 Qwen+2512文生图（4步）极速_2006980155113218050.json、图片生成/文生图/QWEN2512文生图（4步）极速_2008801134533677058.json、图片生成/文生图/QWEN文生图（4步）极速_1995449450854277122.json、图片生成/文生图/QWEN文生图（4步）极速_1996499117574602754.json、图片生成/文生图/QWEN文生图（4步）极速_2075420795974807553.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 14 个 workflow 都包含：
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
- `PreviewImage` —— 12/14 个有
- `ImageScaleBy` —— 10/14 个有
- `VAEEncodeTiled` —— 10/14 个有
- `ImageFromBatch` —— 4/14 个有
- `LayerColor: BrightnessContrastV2` —— 3/14 个有
- `Fooocus positive` —— 1/14 个有
- `ImpactSwitch` —— 1/14 个有
- `LoadImage` —— 1/14 个有
- `Qwen2.5VL` —— 1/14 个有
- `ZML_LoadImage` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 10 | 14 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 79% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 0.3 - 1 | 14 | 81% |
| 宽度 | 1680 | 1080 - 1920 | 14 | 78% |
| 高度 | 1080 | 720 - 1920 | 14 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 10，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 79%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，14 个样本，取值集中（一致性 81%）
- 宽度 中位数 1680，观测区间 1080 - 1920，14 个样本
- 高度 中位数 1080，观测区间 720 - 1920，14 个样本
- 高发问题（20/14 个样本）：Steps较低可能导致细节不足
