---
name: text_to_image_sampler_clip_unet_89
type: Text To Image
frequency: 7
level: strong
coverage: 0.883143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.2 +lora宠物+文生图_1986964422252015617.json, 图片生成/图生图/krea2图生图工作流_2071600191748272129.json, 图片生成/图生图/pipi提示词反推+Z-Image图生图（洗图）_1998176083553976322.json, 图片生成/图生图/王炸 Z-image-trubo 极速洗图_1993949795630989314.json, 图片生成/文生图/Qwen3反推 _ Wan2.2 文生图_1962523964402712577.json, 图片生成/文生图/Wan2.2 文生图_1954164943279013889.json, 图片生成/文生图/绝美古风 _ wan2.2 _ 生图_1966158255494000641.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_89

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Wan2.2 +lora宠物+文生图_1986964422252015617.json、图片生成/图生图/krea2图生图工作流_2071600191748272129.json、图片生成/图生图/pipi提示词反推+Z-Image图生图（洗图）_1998176083553976322.json、图片生成/图生图/王炸 Z-image-trubo 极速洗图_1993949795630989314.json、图片生成/文生图/Qwen3反推 _ Wan2.2 文生图_1962523964402712577.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `ShowText|pysssss` —— 6/7 个有
- `Anything Everywhere` —— 4/7 个有
- `Anything Everywhere3` —— 4/7 个有
- `ModelSamplingSD3` —— 4/7 个有
- `PathchSageAttentionKJ` —— 4/7 个有
- `RH_Captioner` —— 4/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `Fast Bypasser (rgthree)` —— 3/7 个有
- `JjkText` —— 3/7 个有
- `Mute / Bypass Repeater (rgthree)` —— 3/7 个有
- `Text Concatenate (JPS)` —— 3/7 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/7 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/7 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/7 个有
- `ImageConcanate` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `RH_Captioner_Pro` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 7 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | res_2s | - | 7 | 57% |
| 调度器 | bong_tangent | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 864 - 1504 | 7 | 82% |
| 高度 | 1536 | 1504 - 1920 | 7 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，7 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，7 个样本，一致性 57%
- 调度器 最常用 bong_tangent，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 864 - 1504，7 个样本，取值集中（一致性 82%）
- 高度 中位数 1536，观测区间 1504 - 1920，7 个样本，取值集中（一致性 91%）
- 高发问题（13/7 个样本）：Steps较低可能导致细节不足
