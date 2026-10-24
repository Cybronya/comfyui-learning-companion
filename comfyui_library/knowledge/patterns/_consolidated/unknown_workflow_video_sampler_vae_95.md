---
name: unknown_workflow_video_sampler_vae_95
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.958333
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/【自定义Wan2.1万相】文生视频_1901660787495346177.json, 视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json, 视频生成/文生视频/万相2.1文生视频，可控性超强_1907671581512855554.json, 视频生成/文生视频/通义万相 WAN2.1 文生视频，超高可控性_1894646862492905473.json, 视频生成/文生视频/通义万相 文生图工作流-小宣喧 -RH_1894608598201204738.json, 视频生成/文生视频/通义万相Wan2.1文生视频高清补帧放大_1897231501354815489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_95

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/【自定义Wan2.1万相】文生视频_1901660787495346177.json、视频生成/文生视频/【遇见AI】wan2.1文生视频基础流，不带加速_2061012769037701122.json、视频生成/文生视频/万相2.1文生视频，可控性超强_1907671581512855554.json、视频生成/文生视频/通义万相 WAN2.1 文生视频，超高可控性_1894646862492905473.json、视频生成/文生视频/通义万相 文生图工作流-小宣喧 -RH_1894608598201204738.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoBlockSwap` —— 5/6 个有
- `RIFE VFI` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `CR Upscale Image` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `LoadAudio` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
