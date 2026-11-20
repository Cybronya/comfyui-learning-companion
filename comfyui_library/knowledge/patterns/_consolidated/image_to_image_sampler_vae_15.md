---
name: image_to_image_sampler_vae_15
type: Image To Image
frequency: 9
level: strong
coverage: 0.799444
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: CropByMask V2, LoadImage, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku-QWEN-IP角色多视图_2034887755750182914.json, 图片生成/图生图/一图生成角色多视角参考Nunchaku-QWEN_2028292813716201474.json, 图片生成/图生图/一键制作角色多视角（三视图）OK_1987881086120300545.json, 图片生成/图生图/一键制作角色多视角（三视图）_1987355916074987522.json, 图片生成/图生图/千问 IP动漫 四视图  2_2001896485505646593.json, 图片生成/图生图/四视图工作流_2036347779198492674.json, 图片生成/图生图/图片一键多视角工作流_2026582946802573314.json, 图片生成/图生图/🤖Nunchaku-QWEN-IP角色多视图_1988845823905640449.json, 图片生成/文生图/Qwen-Image-Edit三视图Character_Sheet_1985126473839366145.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Nunchaku-QWEN-IP角色多视图_2034887755750182914.json、图片生成/图生图/一图生成角色多视角参考Nunchaku-QWEN_2028292813716201474.json、图片生成/图生图/一键制作角色多视角（三视图）OK_1987881086120300545.json、图片生成/图生图/一键制作角色多视角（三视图）_1987355916074987522.json、图片生成/图生图/千问 IP动漫 四视图  2_2001896485505646593.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 8/9 个有
- `ImageScaleToTotalPixels` —— 8/9 个有
- `INTConstant` —— 7/9 个有
- `ImageUpscaleWithModel` —— 7/9 个有
- `UpscaleModelLoader` —— 7/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `UNETLoader` —— 5/9 个有
- `NunchakuQwenImageDiTLoader` —— 4/9 个有
- `NunchakuQwenImageLoraLoader` —— 4/9 个有
- `RMBG` —— 4/9 个有
- `easy imageRemBg` —— 4/9 个有
- `Anything Everywhere` —— 1/9 个有
- `GoogleTranslateTextNode` —— 1/9 个有
- `LayerMask: RemBgUltra` —— 1/9 个有
- `MaskPreview` —— 1/9 个有
- `easy imageConcat` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 9 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | disable | - | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 36/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 最常用 disable，3 个样本，一致性 100%
- 高发问题（36/9 个样本）：Steps较低可能导致细节不足
