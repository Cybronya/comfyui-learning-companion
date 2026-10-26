---
name: text_to_image_sampler_clip_unet_27
type: Text To Image
frequency: 16
level: weak
coverage: 0.93075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/API-z-image-my_2046050393880272898.json, 图片生成/文生图/API-z-image_2066009097937448961.json, 图片生成/文生图/API-z-image_2066893780837560322.json, 图片生成/文生图/API-z-image_2085310412328886273.json, 图片生成/文生图/API-z-image_2100574150950739970.json, 图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json, 图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json, 图片生成/文生图/Anima Base 复古动漫文生图_2078659623917277185.json, 图片生成/文生图/Anima HiresFix 1.5倍精修_2060759010810355714.json, 图片生成/文生图/Anima Turbo 10-Step｜10步极速文生图_2075555632480079873.json, 图片生成/文生图/Anima正式版-文生图工作流_2055330143593345026.json, 图片生成/文生图/Anima正式版-文生图工作流_2084627398477303810.json, 图片生成/文生图/Anima正式版-文生图工作流个人自用_2076592631471230977.json, 图片生成/文生图/Boogu-Image  Turbo 文生图工作流_2078878116965081089.json, 图片生成/文生图/Krea2 Turbo文生图（双采版）_2070846138026119169.json, 图片生成/文生图/Qwen_image_文生图_1977747366285561858.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_27

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/API-z-image-my_2046050393880272898.json、图片生成/文生图/API-z-image_2066009097937448961.json、图片生成/文生图/API-z-image_2066893780837560322.json、图片生成/文生图/API-z-image_2085310412328886273.json、图片生成/文生图/API-z-image_2100574150950739970.json…）

- **类型**：Text To Image
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

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
- `ConditioningZeroOut` —— 8/16 个有
- `Int` —— 8/16 个有
- `ModelSamplingAuraFlow` —— 5/16 个有
- `Text _O` —— 5/16 个有
- `PreviewImage` —— 3/16 个有
- `Anything Everywhere3` —— 1/16 个有
- `CR Latent Batch Size` —— 1/16 个有
- `LatentUpscale` —— 1/16 个有
- `LoraLoaderModelOnly` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `easy seed` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2416 | 16 | 56% |
| 高度 | 1080 | 1024 - 1920 | 16 | 76% |
| 采样步数 | 16 | 4 - 40 | 16 | 44% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4.5 | 16 | 39% |
| 采样算法 | euler | - | 16 | 69% |
| 调度器 | simple | - | 16 | 88% |
| 重绘幅度 | 1 | 0.35 - 1 | 16 | 78% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2416，16 个样本
- 高度 中位数 1080，观测区间 1024 - 1920，16 个样本
- 采样步数 中位数 16，观测区间 4 - 40，16 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4.5，16 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，16 个样本，一致性 69%
- 调度器 最常用 simple，16 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，16 个样本
