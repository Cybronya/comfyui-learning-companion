---
name: unknown_workflow_video_sampler_unet_12
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.492762
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274.json, 视频生成/文生视频/MiniMax H3 FL2VA开源版-文生视频-自动提示词_2084463867618488321.json, 视频生成/文生视频/MiniMax H3 I2V 图生视频 1280分辨率加速工作流_2085953821150367746.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084242586428067841.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084535052926545922.json, 视频生成/文生视频/MiniMax H3 T2V（文生视频）_2092541585006354433.json, 视频生成/文生视频/MiniMax H3 手机取物换装 文生视频_2106940320041750529.json, 视频生成/文生视频/MiniMax H3 文生视频_2090311300034424833.json, 视频生成/文生视频/MiniMax H3(全能多图参考生视频)4步Lora超级加速版_2085360950907064321.json, 视频生成/文生视频/MiniMax H3+lightx2v 高动态8步加速流+全节点注释_2087717153515597826.json, 视频生成/文生视频/MiniMax H34步Lora超级加速版全能多图参考生视频_2085458700025815041.json, 视频生成/文生视频/MiniMax H3文生视频-电商带货-手机取物换装_2107724379915374594.json, 视频生成/文生视频/MiniMax+H3  9 图_2085645558315831298.json, 视频生成/文生视频/MiniMax+H3文生视频_2089205361046810625.json, 视频生成/文生视频/MiniMax-H3开源 文生视频_2094359561212882945.json, 视频生成/文生视频/MiniMax-H3开源 文生视频_2094381288823287810.json, 视频生成/文生视频/MiniMax_H3_手机取物换装_文生视频_2107269860387545089.json, 视频生成/文生视频/MiniMax_H3_手机取物换装_文生视频_2107472060179107841.json, 视频生成/文生视频/【中近景特写使用】MiniMax H3单采去油腻_2094069348838232066.json, 视频生成/文生视频/【中远景使用】MiniMax H3 双采去油腻_2094069310686846977.json, 视频生成/文生视频/动漫短剧文戏最佳组合（混合模型+结构lora+二采潜空间放大）_2094308569922498562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 FL2VA-Lightx2v-官方4步加速lora-V0.1-文生视频_2086089679518134274.json、视频生成/文生视频/MiniMax H3 FL2VA开源版-文生视频-自动提示词_2084463867618488321.json、视频生成/文生视频/MiniMax H3 I2V 图生视频 1280分辨率加速工作流_2085953821150367746.json、视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084242586428067841.json、视频生成/文生视频/MiniMax H3 T2V（文生视频）_2084535052926545922.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 21 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Text` —— 20/21 个有
- `GetNode` —— 18/21 个有
- `SetNode` —— 18/21 个有
- `LoraLoaderModelOnly` —— 17/21 个有
- `PrimitiveFloat` —— 17/21 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 16/21 个有
- `MiniMaxH3ImageToVideo` —— 14/21 个有
- `LoadImage` —— 10/21 个有
- `MiniMaxH3ReferenceToVideo` —— 7/21 个有
- `ModelAttentionBackend` —— 7/21 个有
- `孤海注释` —— 5/21 个有
- `Float` —— 4/21 个有
- `Label (rgthree)` —— 4/21 个有
- `SigmasGraph` —— 3/21 个有
- `SplitSigmas` —— 3/21 个有
- `VHS_LoadVideoFFmpeg` —— 3/21 个有
- `EmptyImage` —— 2/21 个有
- `Fast Groups Bypasser (rgthree)` —— 2/21 个有
- `LTXVConcatAVLatent` —— 2/21 个有
- `LTXVSeparateAVLatent` —— 2/21 个有
- `MinimaxH3LatentUpscaler3D` —— 2/21 个有
- `PathchSageAttentionKJ` —— 2/21 个有
- `PreviewImage` —— 2/21 个有
- `CR Text` —— 1/21 个有
- `Text Multiline` —— 1/21 个有
- `easy float` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
