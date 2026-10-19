---
name: unknown_workflow_video_sampler_clip_155
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6305
common_nodes: [Anything Everywhere, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1908039126187450370.json, 视频生成/图生视频/1907390680300154882.json, 视频生成/图生视频/1910864267745161217.json, 视频生成/文生视频/1907817176102019074.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_155

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1908039126187450370.json、视频生成/图生视频/1907390680300154882.json、视频生成/图生视频/1910864267745161217.json、视频生成/文生视频/1907817176102019074.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `workflow>3` —— 3/4 个有
- `workflow>4` —— 3/4 个有
- `workflow>5` —— 3/4 个有
- `workflow>6` —— 3/4 个有
- `CR Upscale Image` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `EmptyHunyuanLatentVideo` —— 1/4 个有
- `Int` —— 1/4 个有
- `workflow>1` —— 1/4 个有
- `workflow>2` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
