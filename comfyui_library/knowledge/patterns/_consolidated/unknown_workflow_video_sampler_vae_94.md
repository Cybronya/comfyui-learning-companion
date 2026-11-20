---
name: unknown_workflow_video_sampler_vae_94
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 1
common_nodes: [LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.1 视频转视频（视频风格、动作模仿）工作流_1991468942290010114.json, 平台全量/Wan2.1-KJ-视频到视频编辑_1895342414981169154.json, 平台全量/Wan2.1（阿里万相）视频转视频_1904483791740796930.json, 平台全量/Wan2.2-视频转视频720P_1970385610391363585.json, 平台全量/wan2.2 视频转绘生成一镜到底vlog_1955563712885264385.json, 数字人/数字人/wan2.2 视频转绘生成一镜到底vlog_1954830072336179202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_94

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Wan2.1 视频转视频（视频风格、动作模仿）工作流_1991468942290010114.json、平台全量/Wan2.1-KJ-视频到视频编辑_1895342414981169154.json、平台全量/Wan2.1（阿里万相）视频转视频_1904483791740796930.json、平台全量/Wan2.2-视频转视频720P_1970385610391363585.json、平台全量/wan2.2 视频转绘生成一镜到底vlog_1955563712885264385.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/6 个有
- `ImageResizeKJ` —— 4/6 个有
- `WanVideoBlockSwap` —— 4/6 个有
- `WanVideoContextOptions` —— 3/6 个有
- `WanVideoLoraSelect` —— 3/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `CM_IntToFloat` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `Primitive string [Crystools]` —— 1/6 个有
- `VHS_VideoInfo` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
