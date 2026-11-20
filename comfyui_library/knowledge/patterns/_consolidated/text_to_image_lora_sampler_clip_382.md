---
name: text_to_image_lora_sampler_clip_382
type: Text To Image
frequency: 5
level: strong
coverage: 0.853
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1姿态编辑图生图处理生成工具_2102549583330111489.json, 图片生成/图生图/Qwen Image 2.1材质迁移｜金属木质一键换质感｜设计素材秒变新风格_2102599156345958401.json, 图片生成/图生图/Qwen Image 2.1纯净官流编辑｜40步无PE稳定出图_2103104435521155074.json, 图片生成/图生图/Qwen Image 2.1编辑纯净官流40步无PE，搭配技能使用效果更佳_2103199505092014082.json, 图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_382

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1姿态编辑图生图处理生成工具_2102549583330111489.json、图片生成/图生图/Qwen Image 2.1材质迁移｜金属木质一键换质感｜设计素材秒变新风格_2102599156345958401.json、图片生成/图生图/Qwen Image 2.1纯净官流编辑｜40步无PE稳定出图_2103104435521155074.json、图片生成/图生图/Qwen Image 2.1编辑纯净官流40步无PE，搭配技能使用效果更佳_2103199505092014082.json、图片生成/文生图/Qwen Image 2.1文生图纯净官流40步无PE，搭配技能高质量文本出图方案_2103260563735400450.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `PrimitiveStringMultiline` —— 4/5 个有
- `ResolutionSelector` —— 4/5 个有
- `ComfySwitchNode` —— 3/5 个有
- `PixaromaSeed` —— 3/5 个有
- `PrimitiveBoolean` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 2/5 个有
- `PixaromaRunTimer` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `QwenImage21Cache` —— 2/5 个有
- `GetImageSize` —— 1/5 个有
- `GroupSwitcher` —— 1/5 个有
- `NuiKr.OpenPoseEditor` —— 1/5 个有
- `OpenposePreprocessor` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
