---
name: text_to_image_upscale_sampler_clip_9
type: Text To Image
frequency: 7
level: strong
coverage: 0.851
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-Image+lora文生图.json_2092039413546176513.json, 图片生成/文生图/260708001.Z-image笑着哭反差少女_2074649554405912578.json, 图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图001.Z-Image+lora文生图带放大_2021966017785761793.json, 图片生成/文生图/AA--Zimage文生图-基础+SeedVR2放大_1998702080091152386.json, 图片生成/文生图/Krea 2文生图+高清4K放大_2069681674400653314.json, 图片生成/文生图/Z-Image+lora测试工作流_2027762368310157313.json, 图片生成/文生图/氛围仙侠 分镜_2079113436012830721.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/001.Z-Image+lora文生图.json_2092039413546176513.json、图片生成/文生图/260708001.Z-image笑着哭反差少女_2074649554405912578.json、图片生成/文生图/5.其他类型-6.NSF+-09.Z-image生图001.Z-Image+lora文生图带放大_2021966017785761793.json、图片生成/文生图/AA--Zimage文生图-基础+SeedVR2放大_1998702080091152386.json、图片生成/文生图/Krea 2文生图+高清4K放大_2069681674400653314.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 6/7 个有
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageScaleBy` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `LoraLoader` —— 3/7 个有
- `SetNode` —— 2/7 个有
- `TextInput_` —— 2/7 个有
- `easy promptLine` —— 2/7 个有
- `CR Prompt List` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `InversionDemoLazySwitch` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 10 | 7 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 7 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1080 | 720 - 1280 | 7 | 76% |
| 高度 | 1920 | 1280 - 1920 | 7 | 81% |
| LoRA 模型强度 | 1 | 1 - 2.1 | 3 | 62% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 10，7 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，7 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1280，7 个样本
- 高度 中位数 1920，观测区间 1280 - 1920，7 个样本，取值集中（一致性 81%）
- LoRA 模型强度 中位数 1，观测区间 1 - 2.1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
