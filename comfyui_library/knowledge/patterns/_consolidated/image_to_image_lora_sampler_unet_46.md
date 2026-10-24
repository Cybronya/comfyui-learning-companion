---
name: image_to_image_lora_sampler_unet_46
type: Image To Image
frequency: 12
level: strong
coverage: 0.862167
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit-Instyle图像编辑V0.5_1968547479576825858.json, 图片生成/图生图/QwenEdit-万物竖中指一致性图像编辑V1_1968543069031288833.json, 图片生成/图生图/QwenEdit-电商服装人台V1（不支持真人）_1968545752215629825.json, 图片生成/图生图/Qwen_Edit_2511多图改图_2055553864379715585.json, 图片生成/图生图/Qwen_Edit_2511多角度_2055560720015732738.json, 图片生成/图生图/Qwen_Edit_2511多角度同出_2056331114276540418.json, 图片生成/图生图/Qwen_Edit_2511改图_2055536614876688385.json, 图片生成/图生图/Qwen_Multiangle_2511图片角度自由控制_2010971058458861569.json, 图片生成/图生图/Qwen_Multiangle_2511图片角度自由控制_2038483773788000257.json, 图片生成/图生图/qwen  分镜 精准镜头视角控制器  模特套图 商品套图_2046923407031275521.json, 图片生成/图生图/qwen2511改图工作流_2038270042151849986.json, 图片生成/图生图/qwen2511角度控制_2003687770960871425.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_46

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/QwenEdit-Instyle图像编辑V0.5_1968547479576825858.json、图片生成/图生图/QwenEdit-万物竖中指一致性图像编辑V1_1968543069031288833.json、图片生成/图生图/QwenEdit-电商服装人台V1（不支持真人）_1968545752215629825.json、图片生成/图生图/Qwen_Edit_2511多图改图_2055553864379715585.json、图片生成/图生图/Qwen_Edit_2511多角度_2055560720015732738.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 10/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 9/12 个有
- `Image Comparer (rgthree)` —— 9/12 个有
- `ModelSamplingAuraFlow` —— 9/12 个有
- `TextEncodeQwenImageEditPlus` —— 9/12 个有
- `FluxKontextImageScale` —— 8/12 个有
- `easy showAnything` —— 6/12 个有
- `CFGNorm` —— 5/12 个有
- `QwenMultiangleCameraNode` —— 5/12 个有
- `easy promptList` —— 4/12 个有
- `CR Prompt Text` —— 3/12 个有
- `ConditioningZeroOut` —— 3/12 个有
- `ImageConcanate` —— 3/12 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 3/12 个有
- `ImageScaleToTotalPixels` —— 2/12 个有
- `CR Prompt List` —— 1/12 个有
- `Int` —— 1/12 个有
- `PurgeVRAM_UTK` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 12 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，12 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
