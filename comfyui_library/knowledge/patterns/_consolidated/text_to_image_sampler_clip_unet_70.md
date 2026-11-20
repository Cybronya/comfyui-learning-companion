---
name: text_to_image_sampler_clip_unet_70
type: Text To Image
frequency: 9
level: strong
coverage: 0.915778
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2双图风格融合V1_2069784344645947394.json, 图片生成/图生图/boogu+image+turbo-hotfix版-极速文生图-euler与ddim_2074395054931800065.json, 图片生成/图生图/boogu极致美学+image+turbo-hotfix版-极速文生图-euler与ddim_2076512872733167617.json, 图片生成/图生图/极速洗图仿图-boogu image turbo-hotfix版_2073347665429098497.json, 图片生成/图生图/极速洗图仿图-boogu image turbo-hotfix版_2073444834572070913.json, 图片生成/文生图/boogu Turbo Hotfix修复版极速文生图_2072876509190254594.json, 图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2073336372441739265.json, 图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2073991622328668161.json, 图片生成/文生图/boogu image turbo-hotfix版-极速文生图-euler与ddim_2074374671864258562.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_70

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Krea2双图风格融合V1_2069784344645947394.json、图片生成/图生图/boogu+image+turbo-hotfix版-极速文生图-euler与ddim_2074395054931800065.json、图片生成/图生图/boogu极致美学+image+turbo-hotfix版-极速文生图-euler与ddim_2076512872733167617.json、图片生成/图生图/极速洗图仿图-boogu image turbo-hotfix版_2073347665429098497.json、图片生成/图生图/极速洗图仿图-boogu image turbo-hotfix版_2073444834572070913.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 8/9 个有
- `easy seed` —— 8/9 个有
- `CR Prompt Text` —— 7/9 个有
- `PreviewAny` —— 7/9 个有
- `QwenImageEngineer` —— 6/9 个有
- `LoadImage` —— 4/9 个有
- `RH_LLMAPI_Pro_Node` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `easy imageConcat` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有
- `RH_Captioner` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 9 | 100% |
| 高度 | 1024 | 1024 - 1024 | 9 | 100% |
| 采样步数 | 4 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | ddim | - | 9 | 89% |
| 调度器 | beta57 | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ddim，9 个样本，一致性 89%
- 调度器 最常用 beta57，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（16/9 个样本）：Steps较低可能导致细节不足
