---
name: image_to_image_sampler_clip_unet_24
type: Image To Image
frequency: 11
level: strong
coverage: 0.878091
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Kontext-本地版-中文输入_1962530753999450114.json, 图片生成/图生图/Kontext-生成产品背景_1943184610207686657.json, 图片生成/图生图/Kontext-生成产品背景_1971036089194553346.json, 图片生成/图生图/Kontext【一键】提取线稿，适合二创_1958351836795310082.json, 图片生成/图生图/Kontext一句话转换风格（主体特征不变）_1942037287171735554.json, 图片生成/图生图/ai性别大反转男生转女生_1944259274073604097.json, 图片生成/图生图/flux 一键参考生成图像_1928839789221679106.json, 图片生成/图生图/flux-kontext 高精度换脸工作流_1965603567757312002.json, 图片生成/图生图/老照片修复(全能)_2041505459147902978.json, 图片生成/图生图/老照片修复_1992160042147270657.json, 图片生成/图生图/老照片修复_Kontext-DEV开源ComfyUI官方版_1938389131972247553.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_24

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Kontext-本地版-中文输入_1962530753999450114.json、图片生成/图生图/Kontext-生成产品背景_1943184610207686657.json、图片生成/图生图/Kontext-生成产品背景_1971036089194553346.json、图片生成/图生图/Kontext【一键】提取线稿，适合二创_1958351836795310082.json、图片生成/图生图/Kontext一句话转换风格（主体特征不变）_1942037287171735554.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 9/11 个有
- `FluxKontextImageScale` —— 8/11 个有
- `GoogleTranslateTextNode` —— 5/11 个有
- `ImageStitch` —— 4/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `easy imageConcat` —— 4/11 个有
- `GetNode` —— 3/11 个有
- `ImageConcatMulti` —— 3/11 个有
- `RH_Translator` —— 3/11 个有
- `RepeatLatentBatch` —— 3/11 个有
- `SetNode` —— 3/11 个有
- `ShowText|pysssss` —— 3/11 个有
- `Text Multiline` —— 3/11 个有
- `ShowText` —— 2/11 个有
- `TeaCache` —— 2/11 个有
- `LoaderGGUF` —— 1/11 个有
- `PDIMAGE_LongerSize` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 11 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，11 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
