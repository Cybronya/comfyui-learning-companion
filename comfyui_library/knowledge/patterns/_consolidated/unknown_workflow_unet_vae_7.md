---
name: unknown_workflow_unet_vae_7
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.801364
common_nodes: [CLIPLoader, CreateVideo, PreviewAny, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/minimax_h3_director_r2v_2098743527860690945.json, 平台全量/H3导演台 - 视频编辑模式_2099347188588568578.json, 平台全量/MV_r2v_2120354151875047425.json, 平台全量/MiniMax H3 导演台全能工作流_2088070539373006849.json, 平台全量/MiniMax H3 导演台全能工作流_2090691299413422082.json, 平台全量/MiniMax H3 导演台全能工作流_2101894231005679617.json, 平台全量/MiniMax H3 导演台循环工作台 生成长视频_2118001489410088961.json, 平台全量/Minimax H3 AI长视频导演台二采+脸部修复（短剧、漫剧人物一致、分镜丝滑衔接）_2117081363663904770.json, 平台全量/Minimax_H3_AI长视频导演台二采+脸部修复短剧、漫剧人物一致、分镜丝滑衔接_2117755936730345473.json, 平台全量/Minimax_H3_AI长视频导演台二采+脸部修复（短剧、漫剧人物一致、分镜丝滑衔接）_2117783984968130562.json, 视频生成/文生视频/minimax_h3_director_导演台全能工作流_2102804572346609666.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_7

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/minimax_h3_director_r2v_2098743527860690945.json、平台全量/H3导演台 - 视频编辑模式_2099347188588568578.json、平台全量/MV_r2v_2120354151875047425.json、平台全量/MiniMax H3 导演台全能工作流_2088070539373006849.json、平台全量/MiniMax H3 导演台全能工作流_2090691299413422082.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 9/11 个有
- `PathchSageAttentionKJ` —— 9/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `MiniMaxH3Director` —— 8/11 个有
- `BasicScheduler` —— 7/11 个有
- `MiniMaxH3DirectorRefine` —— 7/11 个有
- `MiniMaxH3DirectorFaceRefine` —— 6/11 个有
- `MiniMaxH3DirectorSelfLift` —— 6/11 个有
- `ComfyMiniMaxH3Director` —— 3/11 个有
- `MiniMaxH3EasyModelAdapter` —— 3/11 个有
- `MiniMaxH3TurboLoRA` —— 3/11 个有
- `ModelAttentionBackend` —— 3/11 个有
- `UpscaleModelLoader` —— 3/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
