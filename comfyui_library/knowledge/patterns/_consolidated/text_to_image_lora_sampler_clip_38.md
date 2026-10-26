---
name: text_to_image_lora_sampler_clip_38
type: Text To Image
frequency: 20
level: strong
coverage: 0.8898
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/DeepSeek最新单品图像处理 智能转换生成工具_2113358859178958849.json, 图片生成/图生图/DeepSeek最新单品工作流， 处理方案_2105805028530409473.json, 图片生成/图生图/G-image2低价版图生图｜低成本高质量出图方案_2098715664189054978.json, 图片生成/图生图/G2图像编辑低价官方版-图生图工作流_2087389684388425730.json, 图片生成/图生图/G2图生图处理生成工具包集_2100669057442869249.json, 图片生成/图生图/Seedream 5.0 Pro图像生成｜图生图直出高清_2090875008297029634.json, 图片生成/图生图/Seedream 5.0 Pro图生图 高质量参考图生成_2105037921689628673.json, 图片生成/图生图/Seedream 5.0 Pro图生图 高质量参考图生成_2109024374207639553.json, 图片生成/图生图/Seedream 5.0 Pro图生图 高质量图像生成方案_2110370093208268802.json, 图片生成/图生图/Seedream 5.0 Pro图生图 高质量图像转换处理工具_2114072462471290882.json, 图片生成/图生图/Seedream 5.0 Pro图生图处理生成工具_2102161720235089921.json, 图片生成/图生图/Seedream 5.0 Pro图生图工作流，图生图高质量图像处理方案_2107523987097088001.json, 图片生成/图生图/Seedream 5.0 Pro图生图，参考图风格化再创作出高质量图_2112651686538993666.json, 图片生成/图生图/qk多场景图工作流 多场景批量生成方案一键搞定_2105133139034202113.json, 图片生成/图生图/qk适用步骤图工作流 分步骤出图方案高效稳定_2105027127480512514.json, 图片生成/图生图/图生图图片编辑｜Seedream 5.0 Pro工作流_2088385877457330178.json, 图片生成/图生图/图生图｜Seedream 5.0 Pro重绘高质量，细节还原度拉满_2099869989200293890.json, 图片生成/图生图/多图适用步骤演示图生成｜流程展示一键出图工作流_2094563805190774786.json, 图片生成/图生图/尺寸图工作流 图片尺寸精准控制一键出图方案_2105130072897318913.json, 图片生成/图生图/最新单品deepseek 图像编辑方案高质量_2109433966536253442.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/DeepSeek最新单品图像处理 智能转换生成工具_2113358859178958849.json、图片生成/图生图/DeepSeek最新单品工作流， 处理方案_2105805028530409473.json、图片生成/图生图/G-image2低价版图生图｜低成本高质量出图方案_2098715664189054978.json、图片生成/图生图/G2图像编辑低价官方版-图生图工作流_2087389684388425730.json、图片生成/图生图/G2图生图处理生成工具包集_2100669057442869249.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 20 个 workflow 都包含：
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
- `Text` —— 17/20 个有
- `RH_SeedreamV5ProImageToImage` —— 10/20 个有
- `JWStringConcat` —— 7/20 个有
- `JjkShowText` —— 3/20 个有
- `RH_LLMAPI_NODE` —— 3/20 个有
- `RH_RhartImageG25FlareImageToImage` —— 3/20 个有
- `SaveText` —— 3/20 个有
- `VRGDG_LocalLLM` —— 3/20 个有
- `RH_RhartImageG2ImageToImage` —— 2/20 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/20 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 20 | 100% |
| 采样算法 | er_sde | - | 20 | 100% |
| 调度器 | beta | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |
| 宽度 | 80 | 80 - 80 | 20 | 100% |
| 高度 | 80 | 80 - 80 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，20 个样本，一致性 100%
- 调度器 最常用 beta，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，20 个样本，取值集中（一致性 100%）
- 高发问题（20/20 个样本）：Steps较低可能导致细节不足
