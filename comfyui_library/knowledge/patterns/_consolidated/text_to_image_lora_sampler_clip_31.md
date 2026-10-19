---
name: text_to_image_lora_sampler_clip_31
type: Text To Image
frequency: 17
level: strong
coverage: 0.891765
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3图生视频｜高质量视频生成工作流_2094935914660323330.json, 视频生成/图生视频/MiniMax H3开源图生视频｜FL2VA人物特效运镜生成工作流_2097458572249624578.json, 视频生成/图生视频/MiniMax-H3图生视频RH版首帧驱动｜单图起手直出视频，动起来更自然_2100452638570663938.json, 视频生成/图生视频/MiniMaxH3FL2VA图生视频开源版ENGENGENG_2087148465603301378.json, 视频生成/图生视频/MiniMaxH3开源版图生视频ENGENG_2087138788249264130.json, 视频生成/图生视频/MiniMaxH3首帧生视频图生视频_2087405631845261314.json, 视频生成/图生视频/Minimax H3首尾帧自动提示词-转场场景特效图生视频_2087362211432976385.json, 视频生成/图生视频/图生视频｜MiniMax H3图片转视频工作流_2088348936359731202.json, 视频生成/文生视频/MiniMax H3图生视频开源版处理生成工具_2102142199105409025.json, 视频生成/文生视频/MiniMax H3图生视频开源版｜500+使用量的顶流工作流_2097178870024851457.json, 视频生成/文生视频/MiniMax H3图生视频开源版｜单张图片秒变动态视频_2107664531756507137.json, 视频生成/文生视频/MiniMax H3图生视频首帧生视频开源版工作流，文生视频图生视频处理方案_2108268272717230082.json, 视频生成/文生视频/MiniMax H3图生视频首帧生视频开源版｜首帧起手更可控_2108023968174268417.json, 视频生成/文生视频/MiniMax H3首尾帧视频｜RH开源版可直接上手复现_2107660024502906881.json, 视频生成/文生视频/MiniMax H3首尾帧视频｜RH开源版过渡丝滑不跳帧_2097174241006415873.json, 视频生成/文生视频/开源版图生视频MiniMax文生视频其它视频处理_2085852297464213506.json, 视频生成/文生视频/开源版图生视频Q版萌系｜MiniMax H3文生视频图片转视频_2088374814779207682.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3图生视频｜高质量视频生成工作流_2094935914660323330.json、视频生成/图生视频/MiniMax H3开源图生视频｜FL2VA人物特效运镜生成工作流_2097458572249624578.json、视频生成/图生视频/MiniMax-H3图生视频RH版首帧驱动｜单图起手直出视频，动起来更自然_2100452638570663938.json、视频生成/图生视频/MiniMaxH3FL2VA图生视频开源版ENGENGENG_2087148465603301378.json、视频生成/图生视频/MiniMaxH3开源版图生视频ENGENG_2087138788249264130.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3FL2VAEncode`
- `RHMiniMaxH3FL2VAFirstFrameCondition`
- `RHMiniMaxH3FL2VAModelLoader`
- `RHMiniMaxH3FL2VATarget`
- `RHMiniMaxH3FL2VATextEncoderLoader`
- `RHMiniMaxH3FL2VAVAELoader`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 14/17 个有
- `Int` —— 13/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/17 个有
- `PrimitiveInt` —— 12/17 个有
- `intToFloat _O` —— 11/17 个有
- `ImageResize+` —— 3/17 个有
- `SaveImage` —— 3/17 个有
- `DF_Int_to_Float` —— 1/17 个有
- `EmptyImage` —— 1/17 个有
- `ImageResizeKJv2` —— 1/17 个有
- `ImpactSwitch` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `RHHiddenNodes` —— 1/17 个有
- `RH_LLMAPI_Pro_Node` —— 1/17 个有
- `ShowAnything|Mie` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 17 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 17 | 100% |
| 采样算法 | er_sde | - | 17 | 100% |
| 调度器 | beta | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 80 | 17 | 100% |
| 高度 | 80 | 80 - 80 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，17 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，17 个样本，一致性 100%
- 调度器 最常用 beta，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，17 个样本，取值集中（一致性 100%）
- 高发问题（17/17 个样本）：Steps较低可能导致细节不足
