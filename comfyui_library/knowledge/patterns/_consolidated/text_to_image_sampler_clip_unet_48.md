---
name: text_to_image_sampler_clip_unet_48
type: Text To Image
frequency: 12
level: strong
coverage: 0.865417
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/BOOGU测试_2069366790278434817.json, 图片生成/文生图/Boogu Image 0.1 Turbo Fast Text-to-Image_2072998834151923712.json, 图片生成/文生图/Boogu turbo文生图_2067798697022418945.json, 图片生成/文生图/Boogu 文生图极速版_2069639754718728194.json, 图片生成/文生图/Boogu-Image 0.1 Turbo 极速文生图_2067853157933338626.json, 图片生成/文生图/Boogu-Image 0.1 Turbo_2069099036728184834.json, 图片生成/文生图/Boogu-Image Turbo 文生图 极速版_2068190168858841090.json, 图片生成/文生图/ERNIE-Image文生图工作流_2077952838453514242.json, 图片生成/文生图/Ernie-Image最强生图模型_2046063222658174978.json, 图片生成/文生图/Krea 2_2072697671621636097.json, 图片生成/文生图/Krea2 Turbo + Realism Engineer  V3.1 文生图_2072595346835992577.json, 图片生成/文生图/Krea2-双图风格融合-T8版_2070051493448867842.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_48

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/BOOGU测试_2069366790278434817.json、图片生成/文生图/Boogu Image 0.1 Turbo Fast Text-to-Image_2072998834151923712.json、图片生成/文生图/Boogu turbo文生图_2067798697022418945.json、图片生成/文生图/Boogu 文生图极速版_2069639754718728194.json、图片生成/文生图/Boogu-Image 0.1 Turbo 极速文生图_2067853157933338626.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 8/12 个有
- `ResolutionSelector` —— 4/12 个有
- `PrimitiveStringMultiline` —— 3/12 个有
- `CR Prompt Text` —— 2/12 个有
- `ImageConcanate` —— 2/12 个有
- `LoadImage` —— 2/12 个有
- `CR Seed` —— 1/12 个有
- `LoraLoaderModelOnly` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `easy promptList` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 12 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | lcm | - | 12 | 58% |
| 调度器 | sgm_uniform | - | 12 | 58% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | 768 - 1080 | 12 | 90% |
| 高度 | 1024 | 1024 - 1920 | 12 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，12 个样本，一致性 58%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 58%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1080，12 个样本，取值集中（一致性 90%）
- 高度 中位数 1024，观测区间 1024 - 1920，12 个样本
- 高发问题（16/12 个样本）：Steps较低可能导致细节不足
