---
name: text_to_image_sampler_clip_unet_59
type: Text To Image
frequency: 10
level: weak
coverage: 0.9595
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Anima aesthetic-v11-全底模test-测试工作流_2079220135235252226.json, 图片生成/图生图/Anima base-v11｜10步极速文生图_2079165843375738882.json, 图片生成/图生图/Qwen-厚涂插画_2005961463678337025.json, 图片生成/图生图/Z-image-base文生图-8步-加速版_2029109565865861122.json, 图片生成/图生图/慕沛灵粉红装扮)_1985298677944172546.json, 图片生成/图生图/梦幻孤独画风Qwen_2007044144136462337.json, 图片生成/文生图/2030225062405611521.json, 图片生成/文生图/Anima aesthetic-v11_2080189925386964993.json, 图片生成/文生图/Krea2 文生图_2071762623535861761.json, 图片生成/文生图/Nunchaku Z-Image文生图_2005466390012329986.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Anima aesthetic-v11-全底模test-测试工作流_2079220135235252226.json、图片生成/图生图/Anima base-v11｜10步极速文生图_2079165843375738882.json、图片生成/图生图/Qwen-厚涂插画_2005961463678337025.json、图片生成/图生图/Z-image-base文生图-8步-加速版_2029109565865861122.json、图片生成/图生图/慕沛灵粉红装扮)_1985298677944172546.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `ModelSamplingAuraFlow` —— 7/10 个有
- `PrimitiveStringMultiline` —— 4/10 个有
- `FluxResolutionNode` —— 3/10 个有
- `PDRatioSelector` —— 2/10 个有
- `XB_UNetNameBroadcaster` —— 2/10 个有
- `CFGNorm` —— 1/10 个有
- `CR Latent Input Switch` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `FlashVSRNode` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `NunchakuZImageDiTLoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 10 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 34% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 976 | 512 - 1664 | 10 | 63% |
| 高度 | 824 | 248 - 1664 | 10 | 48% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 34%
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 976，观测区间 512 - 1664，10 个样本
- 高度 中位数 824，观测区间 248 - 1664，10 个样本，取值分散，一致性仅 48%
- 高发问题（9/10 个样本）：Steps较低可能导致细节不足
