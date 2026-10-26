---
name: unknown_workflow_video_sampler_vae_66
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.964571
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/电商定制文生视频_1924016938777759746.json, 视频生成/图生视频/WAN2.1图生视频之变身超级赛亚人_1944414418782572545.json, 视频生成/图生视频/Wan视频-召唤法相2.0_1913798137197330434.json, 视频生成/图生视频/wan2.1 +lora刀切玻璃水果_2006534001057599489.json, 视频生成/图生视频/wan2.1 And lora 刀切玻璃水果蔬菜 图生视频工作流_1935718246421028865.json, 视频生成/图生视频/wan2.1 And lora 刀切玻璃水果蔬菜 图生视频工作流_1950422709600698370.json, 视频生成/图生视频/wan2.1 图生视频工作流(可本地调用)_1913664774507327490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_66

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/电商定制文生视频_1924016938777759746.json、视频生成/图生视频/WAN2.1图生视频之变身超级赛亚人_1944414418782572545.json、视频生成/图生视频/Wan视频-召唤法相2.0_1913798137197330434.json、视频生成/图生视频/wan2.1 +lora刀切玻璃水果_2006534001057599489.json、视频生成/图生视频/wan2.1 And lora 刀切玻璃水果蔬菜 图生视频工作流_1935718246421028865.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `LoadWanVideoClipTextEncoder` —— 6/7 个有
- `WanVideoImageClipEncode` —— 6/7 个有
- `WanVideoLoraSelect` —— 6/7 个有
- `LayerUtility: PurgeVRAM` —— 5/7 个有
- `ImpactInt` —— 3/7 个有
- `JjkText` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `WanVideoExperimentalArgs` —— 3/7 个有
- `WanVideoSLG` —— 3/7 个有
- `WanVideoTeaCache` —— 3/7 个有
- `GetImageSize+` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `Text Multiline` —— 1/7 个有
- `WanVideoEmptyEmbeds` —— 1/7 个有
- `WanVideoEnhanceAVideo` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
