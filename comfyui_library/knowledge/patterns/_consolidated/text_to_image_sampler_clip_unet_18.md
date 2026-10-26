---
name: text_to_image_sampler_clip_unet_18
type: Text To Image
frequency: 21
level: weak
coverage: 0.941143
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima 动漫王者文生图_2057038503191605250.json, 图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json, 图片生成/文生图/anima文生图3lora工作流_2059246446616080386.json, 图片生成/文生图/anima文生图基础工作流_2057116788260954114.json, 图片生成/文生图/b-最新krea2文生图_2070050778475220994.json, 图片生成/文生图/boogu turbo文生图_2067882978142941186.json, 图片生成/文生图/boogu turbo文生图加速版V1_2067837356199202818.json, 图片生成/文生图/boogu turbo文生图加速版V1_2068270357320126466.json, 图片生成/文生图/boogu turbo文生图加速版工作流_2067860195535052801.json, 图片生成/文生图/boogu turbo文生图加速版工作流_2067879436858511361.json, 图片生成/文生图/boogu_base 文生图_2068898981547171841.json, 图片生成/文生图/boogu_turbo_2069417901609799682.json, 图片生成/文生图/boogu_turbo文生图_2068959350126891010.json, 图片生成/文生图/boogu文生图_2069052782014984193.json, 图片生成/文生图/boogu文生图满血版工作流_2067862555661520898.json, 图片生成/文生图/boogu文生图满血版工作流_2067880773423816705.json, 图片生成/文生图/boogu满血版文生图V1_2067838674468958210.json, 图片生成/文生图/boogu满血版文生图V1_2068275477441236993.json, 图片生成/文生图/flux1-krea-文生图_1951258671458234369.json, 图片生成/文生图/krea-2文生图_2070065443259375617.json, 图片生成/文生图/电商文生图 krea2_2079494663781834754.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_18

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/文生图/anima 动漫王者文生图_2057038503191605250.json、图片生成/文生图/anima_base 1.0 Moebius 风格文生图_2073322108050038785.json、图片生成/文生图/anima文生图3lora工作流_2059246446616080386.json、图片生成/文生图/anima文生图基础工作流_2057116788260954114.json、图片生成/文生图/b-最新krea2文生图_2070050778475220994.json…）

- **类型**：Text To Image
- **样本数**：21
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 20/21 个有
- `ConditioningZeroOut` —— 17/21 个有
- `CR Prompt Text` —— 8/21 个有
- `JjkText` —— 8/21 个有
- `RH_Translator` —— 7/21 个有
- `LoraLoaderModelOnly` —— 4/21 个有
- `PrimitiveInt` —— 2/21 个有
- `DualCLIPLoader` —— 1/21 个有
- `Int` —— 1/21 个有
- `LoadImage` —— 1/21 个有
- `ResolutionSelector` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 2 - 50 | 21 | 17% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 21 | 37% |
| 采样算法 | lcm | - | 21 | 33% |
| 调度器 | sgm_uniform | - | 21 | 33% |
| 重绘幅度 | 1 | 0.2 - 1 | 21 | 82% |
| 宽度 | 1024 | 512 - 1920 | 21 | 72% |
| 高度 | 1024 | 512 - 1536 | 21 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 2 - 50，21 个样本，取值分散，一致性仅 17%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，21 个样本，取值分散，一致性仅 37%
- 采样算法 最常用 lcm，21 个样本，一致性 33%
- 调度器 最常用 sgm_uniform，21 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，21 个样本，取值集中（一致性 82%）
- 宽度 中位数 1024，观测区间 512 - 1920，21 个样本
- 高度 中位数 1024，观测区间 512 - 1536，21 个样本
- 高发问题（11/21 个样本）：Steps较低可能导致细节不足
