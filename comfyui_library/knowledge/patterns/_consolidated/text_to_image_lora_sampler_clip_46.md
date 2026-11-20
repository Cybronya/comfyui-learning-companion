---
name: text_to_image_lora_sampler_clip_46
type: Text To Image
frequency: 20
level: strong
coverage: 0.90175
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax_H3_FL2VA开源版图生视频，人物类特效运镜控制灵活_2116819948730404866.json, 视频生成/图生视频/Minimax H3首尾帧自动提示词-转场场景特效图生视频_2087362211432976385.json, 视频生成/图生视频/中文提示词首尾帧参考生视频MiniMax H3图生视频可调时长_2088385544035328001.json, 视频生成/图生视频/图生视频FL2VA开源版｜MiniMax H3人物运镜特效直出_2093463724282699778.json, 视频生成/图生视频/图生视频RH版｜MiniMax-H3 首帧驱动 res_multistep 2.46×加速_2089364964539723777.json, 视频生成/图生视频/图生视频新选择｜MiniMax H3 FL2VA开源版 一键生成人物特效大片_2105473788841390081.json, 视频生成/图生视频/图生视频运镜天花板｜MiniMax H3 FL2VA开源版 人物类特效轻松做_2105483963920896001.json, 视频生成/图生视频/图生视频｜MiniMax H3图片转视频工作流_2088348936359731202.json, 视频生成/图生视频/开源版图生视频｜MiniMax H3一键生成_2093259177249566722.json, 视频生成/图生视频/开源版图生视频｜MiniMax H3单图直出视频生成_2093101351344627713.json, 视频生成/图生视频/视频生成 MiniMax H3 FL2VA开源版｜人物特效运镜图生视频_2097574967008391169.json, 视频生成/图生视频/首尾帧参考生视频中文提示词｜MiniMax H3图生视频工作流_2088356370327359489.json, 视频生成/图生视频/首帧参考生视频开源版｜MiniMax H3图生视频工作流_2087209670313340929.json, 视频生成/文生视频/FL2VA开源版图生视频｜MiniMax H3文生图生视频_2092556160426663937.json, 视频生成/文生视频/MiniMax H3图生视频开源版处理生成工具_2102142199105409025.json, 视频生成/文生视频/MiniMax H3图生视频开源版｜500+使用量的顶流工作流_2097178870024851457.json, 视频生成/文生视频/MiniMax H3图生视频开源版｜单张图片秒变动态视频_2107664531756507137.json, 视频生成/文生视频/MiniMax H3图生视频首帧生视频开源版工作流，文生视频图生视频处理方案_2108268272717230082.json, 视频生成/文生视频/MiniMax H3图生视频首帧生视频开源版｜首帧起手更可控_2108023968174268417.json, 视频生成/文生视频/MiniMax H3开源版｜首尾帧文生视频集合版_2095258376325386242.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/MiniMax_H3_FL2VA开源版图生视频，人物类特效运镜控制灵活_2116819948730404866.json、视频生成/图生视频/Minimax H3首尾帧自动提示词-转场场景特效图生视频_2087362211432976385.json、视频生成/图生视频/中文提示词首尾帧参考生视频MiniMax H3图生视频可调时长_2088385544035328001.json、视频生成/图生视频/图生视频FL2VA开源版｜MiniMax H3人物运镜特效直出_2093463724282699778.json、视频生成/图生视频/图生视频RH版｜MiniMax-H3 首帧驱动 res_multistep 2.46×加速_2089364964539723777.json…）

- **类型**：Text To Image
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 20 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 19/20 个有
- `ImageResize+` —— 12/20 个有
- `Int` —— 10/20 个有
- `CR Text` —— 7/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/20 个有
- `PrimitiveInt` —— 6/20 个有
- `intToFloat _O` —— 6/20 个有
- `ImpactSwitch` —— 4/20 个有
- `PreviewImage` —— 4/20 个有
- `SaveImage` —— 3/20 个有
- `RH_OneShot_Prompter` —— 2/20 个有
- `kkGetImage` —— 2/20 个有
- `ImageResizeKJv2` —— 1/20 个有
- `RHHiddenNodes` —— 1/20 个有
- `RHMiniMaxH3DirectModelLoader` —— 1/20 个有
- `RHMiniMaxH3DirectTextEncoderLoader` —— 1/20 个有
- `RHMiniMaxH3DirectVAELoader` —— 1/20 个有
- `RHMiniMaxH3FL2VALastFrameCondition` —— 1/20 个有
- `RHMiniMaxH3T2VATarget` —— 1/20 个有
- `RHMiniMaxH3T2VATextEncode` —— 1/20 个有
- `RH_LLMAPI_Pro_Node` —— 1/20 个有
- `ShowAnything|Mie` —— 1/20 个有
- `忽略多组孤海` —— 1/20 个有

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
