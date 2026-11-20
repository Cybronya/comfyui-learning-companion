---
name: unknown_workflow_video_sampler_unet_25
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.801833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/MiniMax_H3图生视频自动提示词版!RH普通会员版_2085415100269285377.json, 图片生成/图生图/h3短剧流-多角色对话_2094000700031332353.json, 图片生成/文生图/【阿楚臻选低成本01号】海螺H3全能多参音视频生成（9图3视频3音频）开源版_2085713549330046978.json, 视频生成/图生视频/1图_multi_ref_minimax_h3_i2v_2094711687055241217.json, 视频生成/图生视频/2图_multi_ref_minimax_h3_i2v_2094710093471375361.json, 视频生成/图生视频/3图_multi_ref_minimax_h3_i2v_2092499319101415426.json, 视频生成/图生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-图生视频_2086095379162025986.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-图生视频-自动提示词_2084469087677276162.json, 视频生成/图生视频/MiniMax-H3 首尾帧图生视频_2084637924326465538.json, 视频生成/图生视频/MiniMax_ref2v_imgvideoaudio_2092306138221072386.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2084892402388652033.json, 视频生成/图生视频/Minimax H3多参音视频生成开源版（9图3视频3音频）_2086998199218294786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_25

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/MiniMax_H3图生视频自动提示词版!RH普通会员版_2085415100269285377.json、图片生成/图生图/h3短剧流-多角色对话_2094000700031332353.json、图片生成/文生图/【阿楚臻选低成本01号】海螺H3全能多参音视频生成（9图3视频3音频）开源版_2085713549330046978.json、视频生成/图生视频/1图_multi_ref_minimax_h3_i2v_2094711687055241217.json、视频生成/图生视频/2图_multi_ref_minimax_h3_i2v_2094710093471375361.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 11/12 个有
- `MiniMaxH3ReferenceToVideo` —— 8/12 个有
- `PainterVRAM` —— 8/12 个有
- `LoadAudio` —— 5/12 个有
- `MiniMaxH3ImageToVideo` —— 4/12 个有
- `VHS_LoadVideo` —— 4/12 个有
- `ImageResizeKJv2` —— 3/12 个有
- `LoraLoaderModelOnly` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `YK_LoadImageFromURL` —— 3/12 个有
- `孤海注释` —— 3/12 个有
- `Label (rgthree)` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有
- `llama_cpp_instruct_adv` —— 1/12 个有
- `llama_cpp_model_loader` —— 1/12 个有
- `llama_cpp_parameters` —— 1/12 个有
- `图像缩放V2_孤海` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
