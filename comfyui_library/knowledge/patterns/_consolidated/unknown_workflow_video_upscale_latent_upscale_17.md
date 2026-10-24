---
name: unknown_workflow_video_upscale_latent_upscale_17
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.455
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax+H3图生视频-高清_2096765437517328385.json, 视频生成/文生视频/0905万象+动漫短剧文戏（12秒横屏）_2096159965277933569.json, 视频生成/文生视频/0905万象+动漫短剧文戏（12秒竖屏）_2096418321116786689.json, 视频生成/文生视频/H3 数字人口播工作流｜人物场景图 + 音频生成自然 Vlog 口播视频_2103802643083780098.json, 视频生成/文生视频/H3动作迁移2.0！单图参考版、附精简提示词模板_2100655224817012738.json, 视频生成/文生视频/H3最强二采！吊打SelfLift【欢迎实测！效果没self强你砍我】虚空折叠流系列第4篇_2104256632178954241.json, 视频生成/文生视频/H3最强全能工作流之言出法随_2100045687760187393.json, 视频生成/文生视频/H3最强音频驱动对口型二采，吊打SelfLift_2107840856492429314.json, 视频生成/文生视频/H3至尊工作流之言出法随【金鱼佬框架+吃猪侠定制版】_2097127397882683394.json, 视频生成/文生视频/H3虚幻引擎 赛璐璐风格漫画流-双采FL2-736P高清PRO_2100200797417074689.json, 视频生成/文生视频/Jason_二采_H3-多参考生视频-优化版V2_2108131102580895745.json, 视频生成/文生视频/Jason_二采_H3-多参考生视频-优化版_2095126489397288961.json, 视频生成/文生视频/MiniMax H3 多合一全能生视频极速+二采优化版_2097343290071928833.json, 视频生成/文生视频/MiniMax H3-双采多参考生视频-优化版（解决画面油、一致性、生成慢问题） 用RH最基础的配置_2094800335167639554.json, 视频生成/文生视频/Our_H3_AudioTalking_2Image_1Audio_2103836296480378882.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_17

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMax+H3图生视频-高清_2096765437517328385.json、视频生成/文生视频/0905万象+动漫短剧文戏（12秒横屏）_2096159965277933569.json、视频生成/文生视频/0905万象+动漫短剧文戏（12秒竖屏）_2096418321116786689.json、视频生成/文生视频/H3 数字人口播工作流｜人物场景图 + 音频生成自然 Vlog 口播视频_2103802643083780098.json、视频生成/文生视频/H3动作迁移2.0！单图参考版、附精简提示词模板_2100655224817012738.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `easy float` —— 13/15 个有
- `LoadAudio` —— 12/15 个有
- `VAEDecodeAudio` —— 12/15 个有
- `Text` —— 11/15 个有
- `VHS_LoadVideo` —— 10/15 个有
- `忽略多组孤海` —— 10/15 个有
- `Text Multiline` —— 2/15 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 2/15 个有
- `easy cleanGpuUsed` —— 2/15 个有
- `AudioCrop` —— 1/15 个有
- `CR Text` —— 1/15 个有
- `ComfySwitchNode` —— 1/15 个有
- `Compare` —— 1/15 个有
- `Fans Text Concatenate` —— 1/15 个有
- `GetImageSize` —— 1/15 个有
- `INTConstant` —— 1/15 个有
- `Int` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `MiniMaxH3ImageToVideo` —— 1/15 个有
- `PreviewAudio` —— 1/15 个有
- `Seed Everywhere` —— 1/15 个有
- `SoundFlow_GetLength` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
