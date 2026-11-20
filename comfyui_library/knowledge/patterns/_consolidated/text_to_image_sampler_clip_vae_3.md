---
name: text_to_image_sampler_clip_vae_3
type: Text To Image
frequency: 24
level: weak
coverage: 0.974125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z_IMAGE_BACE_2026986655982297089.json, 图片生成/文生图/boogu_image_base 文生图_1900216622093840386.json, 图片生成/文生图/boogu_image_turbo 文生图_1911034174755799042.json, 图片生成/文生图/boogu_image_turbo_2067441416753737730.json, 图片生成/文生图/boogu_turbo-文生图极速-人像真实感_2070712427402055682.json, 图片生成/文生图/boogu_turbo_2067856663108997122.json, 图片生成/文生图/boogu_turbo_example_2068872865654599681.json, 图片生成/文生图/boogu_turbo_快速出图，支持复杂提示词_2069069696166612994.json, 图片生成/文生图/boogu_turbo_文生图_2068263819142590465.json, 图片生成/文生图/boogu_turbo_文生图_2068962805402923010.json, 图片生成/文生图/boogu_turbo_文生图_2069223329772429313.json, 图片生成/文生图/boogu_turbo_文生图_2069231725925978114.json, 图片生成/文生图/boogu_turbo_文生图_2071491115995455489.json, 图片生成/文生图/boogu_turbo工作流_2067417417038516225.json, 图片生成/文生图/boogu_turbo工作流含提示词_2067780518917271554.json, 图片生成/文生图/boogu_turbo文生图_2068941150962147330.json, 图片生成/文生图/boogu_turbo文生图工作流_2069287215741624322.json, 图片生成/文生图/boogu模型快速出图_2069078655669727234.json, 图片生成/文生图/flux 2文生图 丨电商场景图_1997117365974405121.json, 图片生成/文生图/krea2基础工作流_2071862532075253761.json, 图片生成/文生图/qwen image文生图工作流_1953069809741271041.json, 图片生成/文生图/qwen_image文生图支持中文_1948416477526392833.json, 图片生成/文生图/z image 文生图 - 超强随机性_1996217608485617665.json, 图片生成/文生图/☀ Z_image_Turbo 基础文生图_2043121951991930881.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_3

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/文生图/Z_IMAGE_BACE_2026986655982297089.json、图片生成/文生图/boogu_image_base 文生图_1900216622093840386.json、图片生成/文生图/boogu_image_turbo 文生图_1911034174755799042.json、图片生成/文生图/boogu_image_turbo_2067441416753737730.json、图片生成/文生图/boogu_turbo-文生图极速-人像真实感_2070712427402055682.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 23/24 个有
- `ConditioningZeroOut` —— 19/24 个有
- `ModelSamplingAuraFlow` —— 5/24 个有
- `PreviewImage` —— 4/24 个有
- `EnhancedLoadDiffusionModel` —— 1/24 个有
- `FluxGuidance` —— 1/24 个有
- `KSamplerAdvanced` —— 1/24 个有
- `Label (rgthree)` —— 1/24 个有
- `Seed (rgthree)` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 35 | 23 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 24 | 0% |
| 采样算法 | lcm | - | 24 | 62% |
| 调度器 | sgm_uniform | - | 24 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 1024 | 720 - 1200 | 24 | 91% |
| 高度 | 1280 | 1024 - 1920 | 24 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 35，23 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，24 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 lcm，24 个样本，一致性 62%
- 调度器 最常用 sgm_uniform，24 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1200，24 个样本，取值集中（一致性 91%）
- 高度 中位数 1280，观测区间 1024 - 1920，24 个样本，取值集中（一致性 81%）
- 高发问题（18/24 个样本）：Steps较低可能导致细节不足
