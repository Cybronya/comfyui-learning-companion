---
name: text_to_image_sampler_clip_unet_23
type: Text To Image
frequency: 16
level: weak
coverage: 0.85375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2029928001101635585.json, 图片生成/文生图/2029960172382195714.json, 图片生成/文生图/2030250301340520450.json, 图片生成/文生图/47_anima文生图3lora工作流_2062720329054773250.json, 图片生成/文生图/48_anima文生图3lora工作流_2_2063974322926088193.json, 图片生成/文生图/87time # 30  通义千问 QW 中文生成_1938456564812414977.json, 图片生成/文生图/9 个 Krea 2 LoRA 测试_2069657247956946945.json, 图片生成/文生图/Boogu-Image 0.1 Turbo 极速文生图_2067853157933338626.json, 图片生成/文生图/Boogu-Image 0.1 Turbo_2069099036728184834.json, 图片生成/文生图/Boogu-Image Turbo 文生图 VS Zimage-turbo_2069035083775963138.json, 图片生成/文生图/Boogu-Image Turbo 文生图 极速版_2068190168858841090.json, 图片生成/文生图/ERNIE-Image文生图工作流_2077952838453514242.json, 图片生成/文生图/Ernie-Image最强生图模型+全节点注释_2046103239707332609.json, 图片生成/文生图/Ernie-Image最强生图模型_2046063222658174978.json, 图片生成/文生图/Krea 2 反推生图 +LoRA_2080138987389411330.json, 图片生成/文生图/Krea2-二次元模型总控-云端版_2095727543704965121.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_23

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/2029928001101635585.json、图片生成/文生图/2029960172382195714.json、图片生成/文生图/2030250301340520450.json、图片生成/文生图/47_anima文生图3lora工作流_2062720329054773250.json、图片生成/文生图/48_anima文生图3lora工作流_2_2063974322926088193.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/16 个有
- `PreviewImage` —— 8/16 个有
- `LoraLoaderModelOnly` —— 6/16 个有
- `PrimitiveStringMultiline` —— 6/16 个有
- `LoadImage` —— 2/16 个有
- `PrimitiveInt` —— 2/16 个有
- `DownloadAndLoadFlorence2Model` —— 1/16 个有
- `Fast Groups Bypasser (rgthree)` —— 1/16 个有
- `Florence2Run` —— 1/16 个有
- `FluxResolutionNode` —— 1/16 个有
- `ImageConcatMulti` —— 1/16 个有
- `LoraLoader` —— 1/16 个有
- `StringConcatenate` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 16 | 23% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 16 | 29% |
| 采样算法 | euler | - | 16 | 62% |
| 调度器 | simple | - | 16 | 81% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 1024 | 512 - 1280 | 16 | 78% |
| 高度 | 1280 | 512 - 1984 | 16 | 68% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 24/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，16 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，16 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，16 个样本，一致性 62%
- 调度器 最常用 simple，16 个样本，一致性 81%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1280，16 个样本
- 高度 中位数 1280，观测区间 512 - 1984，16 个样本
- 高发问题（24/16 个样本）：Steps较低可能导致细节不足
