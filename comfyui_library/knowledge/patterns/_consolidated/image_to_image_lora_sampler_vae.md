---
name: image_to_image_lora_sampler_vae
type: Image To Image
frequency: 29
level: moderate
coverage: 0.902897
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen  Plus一键文字批量编辑_1971238553831297026.json, 图片生成/图生图/Qwen  Plus一键文字批量编辑_1977345045605031937.json, 图片生成/图生图/Qwen 图片编辑（提示词改图）_1982720861146882049.json, 图片生成/图生图/Qwen-Edit-2509图像编辑_1981990949586903042.json, 图片生成/图生图/Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026.json, 图片生成/图生图/Qwen-Edit_Plus-增强版单图编辑工作流 PK 大香蕉_1971390903992664066.json, 图片生成/图生图/Qwen-Edit_Plus-最强单图海报文字修改工作流_1971390937534513153.json, 图片生成/图生图/Qwen-Splat_2068695747394105345.json, 图片生成/图生图/Qwen2509一键臀部变大_1979457000218202113.json, 图片生成/图生图/QwenEdit Plus专用人物移除偏移修正版V2_1971440289346994178.json, 图片生成/图生图/QwenEdit Plus新版+Nunchaku 4步像素偏移修正版V2（5秒采样）_1971610926044672001.json, 图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V1_1971380157581869058.json, 图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1970873930082881538.json, 图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1971610645382819842.json, 图片生成/图生图/QwenEdit Plus新版偏移修正版V2（换装前置-（自用））_1970892882146140161.json, 图片生成/图生图/QwenEdit Plus新版像素偏移修正加强版V2（Lora加强）_1971897984151646209.json, 图片生成/图生图/QwenEdit Plus新版单图文字修改偏移修正版V1_1971378484037795841.json, 图片生成/图生图/QwenEdit Plus新版单图文字修改偏移修正版V2_1970894512950255618.json, 图片生成/图生图/QwenEdit Plus新版单图文字修改偏移修正版V2，强烈推荐：商用娱乐目前最强！_2021116396561764353.json, 图片生成/图生图/QwenEdit Plus新版单图编辑人物姿态调整偏移修正版V1_1971373133330628610.json, 图片生成/图生图/QwenEdit Plus新版单图编辑人物姿态调整偏移修正版V2_1970887261250297857.json, 图片生成/图生图/QwenEdit Plus新版竖中指偏移修正版V2_1971447299840917505.json, "图片生成/图生图/QwenEditor2511 美甲迁移,快速看美甲效果_2013282613238173698.json", 图片生成/图生图/Qwen美甲迁移_2031193242053644289.json, 图片生成/图生图/qwen2509服装精修_1993578505728442370.json, 图片生成/图生图/qwen2509服装精修_1993602250375446530.json, 图片生成/图生图/qwen2509服装转款式图_1994698688234655745.json, 图片生成/图生图/一键臀部变大Qwen_2015771988760993794.json, 图片生成/文生图/qwen25093d提取v2_1997585061497225218.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（图片生成/图生图/Qwen  Plus一键文字批量编辑_1971238553831297026.json、图片生成/图生图/Qwen  Plus一键文字批量编辑_1977345045605031937.json、图片生成/图生图/Qwen 图片编辑（提示词改图）_1982720861146882049.json、图片生成/图生图/Qwen-Edit-2509图像编辑_1981990949586903042.json、图片生成/图生图/Qwen-Edit-2511版单图&多图融合迁移工作流2.0_2028760934268801026.json…）

- **类型**：Image To Image
- **样本数**：29
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 29 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 25/29 个有
- `EmptySD3LatentImage` —— 25/29 个有
- `Image Comparer (rgthree)` —— 25/29 个有
- `UNETLoader` —— 25/29 个有
- `ImageStitch` —— 24/29 个有
- `TextEncodeQwenImageEdit` —— 24/29 个有
- `DF_Get_image_size` —— 23/29 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 23/29 个有
- `PreviewImage` —— 14/29 个有
- `TextEncodeQwenImageEditPlus` —— 5/29 个有
- `NunchakuQwenImageDiTLoader` —— 4/29 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/29 个有
- `Note _O` —— 1/29 个有
- `PrimitiveStringMultiline` —— 1/29 个有
- `TT_img_enc` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 29 | 56% |
| Prompt 约束强度(CFG) | 1 | 0.8 - 3 | 29 | 65% |
| 采样算法 | euler | - | 29 | 97% |
| 调度器 | simple | - | 29 | 97% |
| 重绘幅度 | 1 | 0.8 - 1 | 29 | 95% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 29/29 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，29 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.8 - 3，29 个样本
- 采样算法 最常用 euler，29 个样本，一致性 97%
- 调度器 最常用 simple，29 个样本，一致性 97%
- 重绘幅度 中位数 1，观测区间 0.8 - 1，29 个样本，取值集中（一致性 95%）
- 风险：Prompt 约束强度(CFG) 观测到 0.8，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 高发问题（29/29 个样本）：Steps较低可能导致细节不足
