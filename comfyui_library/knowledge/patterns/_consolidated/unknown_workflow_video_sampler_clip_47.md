---
name: unknown_workflow_video_sampler_clip_47
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8353
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, ManualSigmas, PainterLTXVtoVideo, PainterSamplerLTXV, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2011647638386515970.json, 视频生成/图生视频/2011652891991351298.json, 视频生成/图生视频/2011690335805644802.json, 视频生成/图生视频/2009113089257508866.json, 视频生成/图生视频/2009463767909801985.json, 视频生成/图生视频/2009226239936040962.json, 视频生成/文生视频/(贞贞lora 4000步)Ltx2高动态智能扩写文生视频V1(Painter精简版)_2011451482868027393.json, 视频生成/文生视频/15-01-03-LTX2.0-文生视频+人物Lora_2012023530224885761.json, 视频生成/文生视频/LTX2.0-文生音视频_2009460170920824833.json, 视频生成/文生视频/Ltx2高动态智能扩写文生视频V1(Painter精简版)_2009218927821332481.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2011647638386515970.json、视频生成/图生视频/2011652891991351298.json、视频生成/图生视频/2011690335805644802.json、视频生成/图生视频/2009113089257508866.json、视频生成/图生视频/2009463767909801985.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `ManualSigmas`
- `PainterLTXVtoVideo`
- `PainterSamplerLTXV`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 9/10 个有
- `RH_LLMAPI_Pro_Node` —— 9/10 个有
- `JWInteger` —— 8/10 个有
- `LoadImage` —— 8/10 个有
- `ShowAnything|Mie` —— 8/10 个有
- `easy anythingIndexSwitch` —— 7/10 个有
- `LoraLoaderModelOnly` —— 5/10 个有
- `ConcatTextOfUtils` —— 4/10 个有
- `GetNode` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
