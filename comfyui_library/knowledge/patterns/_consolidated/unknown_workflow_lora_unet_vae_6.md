---
name: unknown_workflow_lora_unet_vae_6
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.819
common_nodes: [BasicScheduler, CLIPLoader, CreateVideo, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3DirectorRefine, PreviewAny, SaveVideo, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/秋明山自用去油导演台_2100484002187669506.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流 满血版本Ref2va_2097293667320029186.json, 视频生成/文生视频/MiniMax H3 导演台全能工作流 满血版本T2V&FL&I2V修复版_2097354274782138370.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/秋明山自用去油导演台_2100484002187669506.json、视频生成/文生视频/MiniMax H3 导演台全能工作流 满血版本Ref2va_2097293667320029186.json、视频生成/文生视频/MiniMax H3 导演台全能工作流 满血版本T2V&FL&I2V修复版_2097354274782138370.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CreateVideo`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3DirectorRefine`
- `PreviewAny`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UpscaleModelLoader` —— 2/3 个有
- `BlockSparseAttention` —— 1/3 个有
- `EasyCache` —— 1/3 个有
- `MiniMaxLowVRAMAttention` —— 1/3 个有
- `ModelAttentionBackend` —— 1/3 个有
- `SplitSigmas` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
