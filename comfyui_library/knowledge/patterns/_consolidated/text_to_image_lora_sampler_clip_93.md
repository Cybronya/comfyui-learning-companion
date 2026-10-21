---
name: text_to_image_lora_sampler_clip_93
type: Text To Image
frequency: 11
level: strong
coverage: 0.900091
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, RHMiniMaxH3DecodeAV, RHMiniMaxH3DirectModelLoader, RHMiniMaxH3DirectTextEncoderLoader, RHMiniMaxH3DirectVAELoader, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3T2VATarget, RHMiniMaxH3T2VATextEncode, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 FL2VA开源版图生视频 脑洞创意电影感视频生成_2099229846823063553.json, 视频生成/图生视频/开源免费MiniMax H3 FL2VA｜脑洞剧本一键开拍，电影感拉满_2099403535325679617.json, 视频生成/文生视频/FL2VA开源版文生视频｜MiniMax H3一键生成_2093264814079569922.json, 视频生成/文生视频/MiniMax H3开源版文生视频｜视频运镜提示词直出_2089449365793501185.json, 视频生成/文生视频/MiniMax H3文生视频开源版处理生成工具_2102140647884021762.json, 视频生成/文生视频/MiniMax H3文生视频开源版｜一句话生成大片级画面_2107663052278681601.json, 视频生成/文生视频/MiniMax H3文生视频开源版｜运镜丝滑300+人在用_2097177388667990017.json, 视频生成/文生视频/res_multistep 2.46×零质量损加速｜MiniMax-H3文生视频RH版_2089008529712705537.json, 视频生成/文生视频/res_multistep 2.46倍加速零质量损｜MiniMax-H3文生视频RH版含音频_2088688872459952130.json, 视频生成/文生视频/开源版文生视频MiniMax视频运镜其它视频处理_2085851653433028610.json, 视频生成/文生视频/开源版文生视频｜MiniMax H3 视频运镜自由出片_2089266759978274818.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/H3 FL2VA开源版图生视频 脑洞创意电影感视频生成_2099229846823063553.json、视频生成/图生视频/开源免费MiniMax H3 FL2VA｜脑洞剧本一键开拍，电影感拉满_2099403535325679617.json、视频生成/文生视频/FL2VA开源版文生视频｜MiniMax H3一键生成_2093264814079569922.json、视频生成/文生视频/MiniMax H3开源版文生视频｜视频运镜提示词直出_2089449365793501185.json、视频生成/文生视频/MiniMax H3文生视频开源版处理生成工具_2102140647884021762.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DirectModelLoader`
- `RHMiniMaxH3DirectTextEncoderLoader`
- `RHMiniMaxH3DirectVAELoader`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3T2VATarget`
- `RHMiniMaxH3T2VATextEncode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetVideoComponents` —— 6/11 个有
- `VHS_VideoCombine` —— 6/11 个有
- `SaveVideo` —— 5/11 个有
- `SaveImage` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
