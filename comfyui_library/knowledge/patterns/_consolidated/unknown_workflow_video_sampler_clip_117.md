---
name: unknown_workflow_video_sampler_clip_117
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9434
common_nodes: [CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTXVConditioning, LTXVImgToVideo, LTXVScheduler, LoadImage, SamplerCustom, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTXV 0.9.5图生视频工作流_1903736923179880450.json, 视频生成/图生视频/LTXV 10秒图生视频！！最快AI视频模型   UP 楚门的AI世界_1897315393487196161.json, 视频生成/图生视频/LTXV0.9.6-秒级视频生成-图生视频_1897512765190262785.json, 视频生成/图生视频/【目前最快】LTXV 秒级视频生成- i2v_1914129189279334401.json, 视频生成/文生视频/LTXV0.9.6-秒级视频生成-文生视频_1897511691662348290.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_117

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTXV 0.9.5图生视频工作流_1903736923179880450.json、视频生成/图生视频/LTXV 10秒图生视频！！最快AI视频模型   UP 楚门的AI世界_1897315393487196161.json、视频生成/图生视频/LTXV0.9.6-秒级视频生成-图生视频_1897512765190262785.json、视频生成/图生视频/【目前最快】LTXV 秒级视频生成- i2v_1914129189279334401.json、视频生成/文生视频/LTXV0.9.6-秒级视频生成-文生视频_1897511691662348290.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LTXVConditioning`
- `LTXVImgToVideo`
- `LTXVScheduler`
- `LoadImage`
- `SamplerCustom`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 4/5 个有
- `LTXVPromptEnhancer` —— 4/5 个有
- `LTXVPromptEnhancerLoader` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `Primitive integer [Crystools]` —— 3/5 个有
- `CR Text Concatenate` —— 2/5 个有
- `Primitive string [Crystools]` —— 2/5 个有
- `Bjornulf_ShowStringText` —— 1/5 个有
- `EmptyLTXVLatentVideo` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `Text Concatenate` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `TextInput_` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
