---
name: text_to_image_lora_sampler_clip_102
type: Text To Image
frequency: 13
level: strong
coverage: 0.877308
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/SGM2.5抠图测试版 图生图精准人物分割处理_2098717634647908353.json, 图片生成/图生图/Seedream 5.0 Pro图像生成｜图生图直出高清_2090875008297029634.json, 图片生成/图生图/Seedream 5.0 Pro图生图 高质量参考图生成_2105037921689628673.json, 图片生成/图生图/Seedream 5.0 Pro图生图 高质量参考图生成_2109024374207639553.json, 图片生成/图生图/Seedream 5.0 Pro图生图 高质量图像生成方案_2110370093208268802.json, 图片生成/图生图/Seedream 5.0 Pro图生图处理生成工具_2102161720235089921.json, 图片生成/图生图/Seedream 5.0 Pro图生图工作流，图生图高质量图像处理方案_2107523987097088001.json, 图片生成/图生图/Seedream 5.0 Pro图生图，参考图风格化再创作出高质量图_2112651686538993666.json, 图片生成/图生图/Seedream V5 Pro图生图 2K高清画质输出_2098290095404183554.json, 图片生成/图生图/sgm2.5智能抠图测试流｜图生图主体精准分离_2098708507670433794.json, 图片生成/图生图/图生图图片编辑｜Seedream 5.0 Pro工作流_2088385877457330178.json, 图片生成/图生图/图生图｜Seedream 5.0 Pro重绘高质量，细节还原度拉满_2099869989200293890.json, 图片生成/图生图/多图适用步骤演示图生成｜流程展示一键出图工作流_2094563805190774786.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_102

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/SGM2.5抠图测试版 图生图精准人物分割处理_2098717634647908353.json、图片生成/图生图/Seedream 5.0 Pro图像生成｜图生图直出高清_2090875008297029634.json、图片生成/图生图/Seedream 5.0 Pro图生图 高质量参考图生成_2105037921689628673.json、图片生成/图生图/Seedream 5.0 Pro图生图 高质量参考图生成_2109024374207639553.json、图片生成/图生图/Seedream 5.0 Pro图生图 高质量图像生成方案_2110370093208268802.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_SeedreamV5ProImageToImage` —— 10/13 个有
- `Text` —— 10/13 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/13 个有
- `LayerUtility: ImageCombineAlpha` —— 2/13 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `SetNode` —— 2/13 个有
- `JWStringConcat` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
