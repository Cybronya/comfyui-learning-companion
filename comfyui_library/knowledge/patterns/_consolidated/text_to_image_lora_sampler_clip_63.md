---
name: text_to_image_lora_sampler_clip_63
type: Text To Image
frequency: 13
level: strong
coverage: 0.732923
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, Fast Groups Bypasser (rgthree), ImageConcatMulti, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RHLLMChatNode, RHSettingsNode, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/全能图片G-IMAGE-2.5｜API调用智能体，文生图图生图双支持_2099888363720499201.json, 图片生成/文生图/全能图片G2.5 API调用 文生图图生图智能体工作流_2099915210919342081.json, 图片生成/文生图/全能模型 G-IMAGE-2｜API调用文生图图生图 智能体一条龙_2097539000964829185.json, 图片生成/文生图/全能模型 RPO API调用｜文生图图生图 智能体工作流一次跑通_2097534170913402882.json, 图片生成/文生图/全能模型G2 API调用 文生图图生图智能体工作流_2099954583786311681.json, 图片生成/文生图/全能模型G2_API智能体｜文生图图生图一键调用_2101158681109942273.json, 图片生成/文生图/全能模型G2_API调用_文生图图生图智能体工作流_2100928150585831426.json, 图片生成/文生图/全能模型PRO API调用 文生图图生图智能体工作流_2099956228842676225.json, 图片生成/文生图/全能模型PRO_API调用_文生图图生图智能体工作流_2100926119225675778.json, 图片生成/文生图/全能模型RPO API调用｜文生图图生图，智能体工作流一键搞定_2099878562982612993.json, 图片生成/文生图/智能体工作流｜全能图片G-IMAGE-2 API调用，文生图图生图都行_2099877184583327746.json, 视频生成/图生视频/全能模型G2_API调用_文生图图生图智能体工作流_2100185945998979074.json, 视频生成/图生视频/全能模型PRO_API调用_文生图图生图智能体工作流_2100187012849553410.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/全能图片G-IMAGE-2.5｜API调用智能体，文生图图生图双支持_2099888363720499201.json、图片生成/文生图/全能图片G2.5 API调用 文生图图生图智能体工作流_2099915210919342081.json、图片生成/文生图/全能模型 G-IMAGE-2｜API调用文生图图生图 智能体一条龙_2097539000964829185.json、图片生成/文生图/全能模型 RPO API调用｜文生图图生图 智能体工作流一次跑通_2097534170913402882.json、图片生成/文生图/全能模型G2 API调用 文生图图生图智能体工作流_2099954583786311681.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：73%

## 共有节点

全部 13 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcatMulti`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RHLLMChatNode`
- `RHSettingsNode`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `RH_YouchuanTextToImageV82Fast` —— 11/13 个有
- `孤海注释` —— 9/13 个有
- `RH_RhartImageG2OfficialImageToImage` —— 7/13 个有
- `RH_RhartImageG2OfficialTextToImage` —— 6/13 个有
- `EmptyImage` —— 5/13 个有
- `PreviewImage` —— 5/13 个有
- `RH_RhartImageNProOfficialEdit` —— 5/13 个有
- `RH_RhartImageNProOfficialTextToImage` —— 5/13 个有
- `RH_RhartImageG25OfficialTokenSunburstTextToImage` —— 2/13 个有
- `RH_RhartImageG25OfficialTokenFlareEdit` —— 1/13 个有
- `RH_RhartImageG25OfficialTokenFlareTextToImage` —— 1/13 个有
- `RH_RhartImageG25OfficialTokenSunburstEdit` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（14/13 个样本）：Steps较低可能导致细节不足
