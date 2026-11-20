---
name: unknown_workflow_lora_unet_vae_2
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.92585
common_nodes: [CLIPLoader, CreateVideo, LoraLoaderModelOnly, ModelAttentionBackend, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [平台全量/MiniMAX_H3导演台开源版_2117405298389504001.json, 平台全量/Minimax-H3导演台+selflift双采_2118923527356239874.json, 视频生成/图生视频/MiniMAX H3导演台-图生视频服装展示_2099418470462083073.json, 视频生成/图生视频/MiniMAX H3导演台_2092145187165396993.json, 视频生成/图生视频/MiniMAX H3导演台、模特换装-SZ_2115340607588753410.json, 视频生成/图生视频/MiniMAX H3导演台（开源版）_2094633967482916866.json, 视频生成/图生视频/MiniMAX H3导演台（开源版）_2101179356491108354.json, 视频生成/图生视频/MiniMAXH3_2103712202158067714.json, 视频生成/图生视频/MiniMAX_H3导演台开源版_2100409884482297858.json, 视频生成/图生视频/MiniMAX_H3导演台开源版_2100497281777758210.json, 视频生成/图生视频/Minimax H3 AI长视频导演台二采（短剧、漫剧人物一致、分镜丝滑衔接）_2116497725545074690.json, 视频生成/图生视频/Minimax H3 AI长视频导演台（短剧、漫剧人物一致、分镜丝滑衔接）_2092245664636956674.json, 视频生成/图生视频/Minimax H3 AI长视频导演台（短剧、漫剧人物一致、分镜丝滑衔接）_2114673407387324418.json, 视频生成/图生视频/Minimax H3 AI长视频导演台（短剧、漫剧人物一致、极速1080P）_2114751850204450818.json, 视频生成/图生视频/Minimax_H3_AI长视频导演台短剧、漫剧人物一致、分镜丝滑衔接_2101858980703334402.json, 视频生成/图生视频/Minimax_H3_AI长视频导演台短剧、漫剧人物一致、分镜丝滑衔接_2102675010459623425.json, 视频生成/文生视频/Minimax H3 AI长视频导演台（短剧、漫剧人物一致、极速1080P）_2091136510912454657.json, 视频生成/文生视频/Minimax H3 全能导演台（短剧分镜丝滑衔接）_2094785653799211010.json, 视频生成/文生视频/Minimax_H3_AI长视频导演台二采短剧、漫剧人物一致、分镜丝滑衔接_2116671152625111042.json, 视频生成/文生视频/Minimax_H3_AI长视频导演台二采短剧、漫剧人物一致、分镜丝滑衔接_2116683030352977922.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（平台全量/MiniMAX_H3导演台开源版_2117405298389504001.json、平台全量/Minimax-H3导演台+selflift双采_2118923527356239874.json、视频生成/图生视频/MiniMAX H3导演台-图生视频服装展示_2099418470462083073.json、视频生成/图生视频/MiniMAX H3导演台_2092145187165396993.json、视频生成/图生视频/MiniMAX H3导演台、模特换装-SZ_2115340607588753410.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `ModelAttentionBackend`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3TurboLoRA` —— 19/20 个有
- `ComfyMiniMaxH3Director` —— 12/20 个有
- `MiniMaxH3EasyModelAdapter` —— 10/20 个有
- `MiniMaxH3Director` —— 8/20 个有
- `MiniMaxH3DirectorRefine` —— 3/20 个有
- `MiniMaxChunkFeedForward` —— 1/20 个有
- `MiniMaxH3DirectorSelfLift` —— 1/20 个有
- `MiniMaxLowVRAMAttention` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
