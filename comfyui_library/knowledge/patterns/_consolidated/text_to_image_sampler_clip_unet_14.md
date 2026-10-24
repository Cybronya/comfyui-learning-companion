---
name: text_to_image_sampler_clip_unet_14
type: Text To Image
frequency: 20
level: weak
coverage: 0.9525
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/API-z-image-my_2046050393880272898.json, 图片生成/文生图/API-z-image_2066009097937448961.json, 图片生成/文生图/API-z-image_2066893780837560322.json, 图片生成/文生图/API-z-image_2085310412328886273.json, 图片生成/文生图/API-z-image_2100574150950739970.json, 图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json, 图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json, 图片生成/文生图/Anima Base any-test-like控制生图_2073323335081095169.json, 图片生成/文生图/Anima Base 复古动漫文生图_2078659623917277185.json, 图片生成/文生图/Anima Turbo 10-Step｜10步极速文生图_2075555632480079873.json, 图片生成/文生图/Boogu turbo文生图_2067798697022418945.json, 图片生成/文生图/Boogu-Base 高清质感文生图_2068717818228592642.json, 图片生成/文生图/Boogu-Image  Turbo 文生图工作流_2078878116965081089.json, 图片生成/文生图/Boogu-Image Base基础文生图_2068063950163501058.json, 图片生成/文生图/Boogu-Image Turbo基础文生图2606_2068063045523435521.json, 图片生成/文生图/None Z-image-Turbo CFG解锁版（提高高频信息）_1999533655208980481.json, 图片生成/文生图/Z-image-Turbo电影质感文生图_2056911427314737153.json, 图片生成/文生图/z-image-turbo-flow-dpo版文生图_2027731924940230658.json, 图片生成/文生图/墨沫深空krea2-RAW 工作流_2077060951261671426.json, 图片生成/文生图/文生图z-image-turbo+D-OPSD+全节点注释_2056647828327452673.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_14

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/API-z-image-my_2046050393880272898.json、图片生成/文生图/API-z-image_2066009097937448961.json、图片生成/文生图/API-z-image_2066893780837560322.json、图片生成/文生图/API-z-image_2085310412328886273.json、图片生成/文生图/API-z-image_2100574150950739970.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 15/20 个有
- `CR Prompt Text` —— 8/20 个有
- `Int` —— 8/20 个有
- `Text _O` —— 5/20 个有
- `LoraLoaderModelOnly` —— 4/20 个有
- `TTResolutionSelector` —— 3/20 个有
- `easy seed` —— 3/20 个有
- `LoadImage` —— 2/20 个有
- `AnimaLLLiteApply` —— 1/20 个有
- `CustomAddLabel` —— 1/20 个有
- `PreviewImage` —— 1/20 个有
- `RHHiddenNodes` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1052 | 512 - 2416 | 20 | 54% |
| 高度 | 1080 | 512 - 1920 | 20 | 69% |
| 采样步数 | 14 | 4 - 50 | 20 | 26% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 20 | 31% |
| 采样算法 | euler | - | 20 | 65% |
| 调度器 | simple | - | 20 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1052，观测区间 512 - 2416，20 个样本
- 高度 中位数 1080，观测区间 512 - 1920，20 个样本
- 采样步数 中位数 14，观测区间 4 - 50，20 个样本，取值分散，一致性仅 26%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，20 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，20 个样本，一致性 65%
- 调度器 最常用 simple，20 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
